import serial
import pynmea2

UART_PORT = "/dev/ttyAMA0"
BAUD_RATE = 9600


def configure_gps(gps):
    command = bytes([
        0xB5, 0x62,
        0x06, 0x08,
        0x06, 0x00,
        0xE8, 0x03,
        0x01, 0x00,
        0x00, 0x00,
        0x00, 0x37
    ])

    gps.write(command)
    gps.flush()

    print("GPS configured: 1 Hz")


def main():
    gps = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)

    configure_gps(gps)

    print(f"GPS reader started: {UART_PORT} @ {BAUD_RATE}")

    try:
        while True:
            line = gps.readline().decode("ascii", errors="ignore").strip()

            if not line.startswith("$"):
                continue

            try:
                message = pynmea2.parse(line)

                if isinstance(message, pynmea2.types.talker.GGA):
                    print(
                        f"Lat: {message.latitude:.6f}, "
                        f"Lon: {message.longitude:.6f}, "
                        f"Altitude: {message.altitude} m, "
                        f"Satellites: {message.num_sats}, "
                        f"Fix: {message.gps_qual}"
                    )

            except pynmea2.ParseError:
                pass

    except KeyboardInterrupt:
        print("\nGPS reader stopped")

    finally:
        gps.close()


if __name__ == "__main__":
    main()