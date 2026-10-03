# Raspberry Pi GPS Reader

A simple Raspberry Pi project for reading GPS data from a u-blox NEO-6M module over UART.

The application:
- initializes the UART interface;
- configures the GPS module using the UBX protocol;
- continuously reads NMEA messages;
- parses latitude, longitude, altitude, satellite count, and GPS fix status;
- automatically starts on Raspberry Pi boot using `systemd`.

## Hardware

- Raspberry Pi 5
- GY-GPS6MV2 / u-blox NEO-6M GPS module
- Dupont wires

## Wiring

| GPS | Raspberry Pi |
|---|---|
| VCC | Pin 2 — 5V |
| GND | Pin 6 — GND |
| TX | Pin 10 — GPIO15 / RX |
| RX | Pin 8 — GPIO14 / TX |

UART device:

```text
/dev/ttyAMA0