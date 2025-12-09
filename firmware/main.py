#pragma once

#define VENDOR_ID       0xFEED
#define PRODUCT_ID      0x0001
#define DEVICE_VER      0x0001
#define MANUFACTURER    YourName
#define PRODUCT         5Key Macropad

#define MATRIX_ROWS 1
#define MATRIX_COLS 5

#define MATRIX_ROW_PINS { GP1 }
#define MATRIX_COL_PINS { GP1, GP2, GP4, GP3, GP0 }
#define DIODE_DIRECTION COL2ROW

#define ENCODERS_PAD_A { GP29 }
#define ENCODERS_PAD_B { GP28 }
#define ENCODER_RESOLUTION 4

#define ENCODER_BUTTON_PIN GP27

#define RGB_DI_PIN GP26
#define RGBLED_NUM 5
#define RGBLIGHT_ANIMATIONS
#define RGBLIGHT_HUE_STEP 8
#define RGBLIGHT_SAT_STEP 8
#define RGBLIGHT_VAL_STEP 8

#define OLED_DISPLAY_128X32
#define I2C_DRIVER I2CD1
#define I2C1_SDA_PIN GP6
#define I2C1_SCL_PIN GP7

#define DEBOUNCE 5

#include QMK_KEYBOARD_H

enum custom_keycodes {
    KC_ENC_BTN = SAFE_RANGE,
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_1,    KC_2,    KC_3,    KC_4,    KC_5
    )
};

bool encoder_update_user(uint8_t index, bool clockwise) {
    if (clockwise) {
        tap_code(KC_VOLU);
    } else {
        tap_code(KC_VOLD);
    }
    return false;
}

void matrix_scan_user(void) {
    static bool encoder_button_pressed = false;
    bool current_state = !readPin(GP27);
    
    if (current_state && !encoder_button_pressed) {
        tap_code(KC_MUTE);
        encoder_button_pressed = true;
    } else if (!current_state && encoder_button_pressed) {
        encoder_button_pressed = false;
    }
}

#ifdef OLED_ENABLE
oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_0;
}

bool oled_task_user(void) {
    oled_write_P(PSTR("5-Key Macropad\n"), false);
    oled_write_P(PSTR("Layer: "), false);
    oled_write_char('0' + get_highest_layer(layer_state), false);
    oled_write_P(PSTR("\n\n"), false);
    
    oled_write_P(PSTR("RGB: "), false);
    if (rgblight_is_enabled()) {
        oled_write_P(PSTR("ON\n"), false);
    } else {
        oled_write_P(PSTR("OFF\n"), false);
    }
    
    return false;
}
#endif

BOOTMAGIC_ENABLE = yes
MOUSEKEY_ENABLE = yes
EXTRAKEY_ENABLE = yes
CONSOLE_ENABLE = no
COMMAND_ENABLE = no
NKRO_ENABLE = yes
BACKLIGHT_ENABLE = no
RGBLIGHT_ENABLE = yes
ENCODER_ENABLE = yes
OLED_ENABLE = yes
OLED_DRIVER = SSD1306

