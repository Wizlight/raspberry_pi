import serial

UART_PORT = "/dev/ttyAMA0"
BAUD_RATE = 9600


def main():
    gps = serial.Serial(
        port=UART_PORT,
        baudrate=BAUD_RATE,
        timeout=1
    )

    print(f"GPS reader started: {UART_PORT} @ {BAUD_RATE}")

    try:
        while True:
            line = gps.readline().decode("ascii", errors="ignore").strip()

            if line:
                print(line)

    except KeyboardInterrupt:
        print("\nGPS reader stopped")

    finally:
        gps.close()


if __name__ == "__main__":
    main()