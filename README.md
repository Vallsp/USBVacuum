# USBVacuum

An automated malware cleaning station.
![usbvacuum](https://github.com/Vallsp/USBVacuum/assets/145016532/33d703ae-6b31-4df8-a932-4423a548d522)

## Introduction

In an increasingly connected world, USB drives have become essential tools for data storage and transfer. However, with their widespread use, the risks associated with malware carried by these devices have become a major concern for users and organizations.

USBVacuum aims to provide an effective and reliable solution for cleaning USB drives of malware. This automated white station is designed to detect and eliminate potential threats while preserving the integrity of legitimate data.

### Problem Description

USB drives are a common vector for malware propagation. When an infected USB drive is inserted into a system, the malware can spread quickly, compromising network security and sensitive data.

### Objectives and Challenges

1. **Prevent Malware Spread**: Stop the dissemination of malware via USB drives.

2. **Maintain Data Integrity**: Ensure legitimate data remains intact post-cleaning.

3. **User-Friendly**: Provide an easy-to-use solution that requires no technical expertise.

4. **Awareness and Education**: Raise awareness and educate users on safe practices.

### Target Users

- **Employees and network users**: end-users, whether employees of a company or members of an organization. They benefit indirectly from the security provided by the white station, as it helps prevent malware infection and protects their data and IT systems.

- **Information Security Managers**: These professionals are responsible for guaranteeing the confidentiality, integrity and availability of data within the organization. The white station is an invaluable tool in their security arsenal, enabling them to detect and neutralize potential threats as soon as they appear.

## Application Architecture

### Technological Choices

- **Python**: Versatile programming language for rapid application development.

- **Figma**: Cloud-based UI/UX design tool for real-time collaboration.

- **Docker**: Containerization platform ensuring uniform application performance across environments.

- **Tkinter**: Python's standard GUI library for building simple interfaces.

## Features

### USB Detection

Automatically initiates a scan when a USB drive is inserted.

### Display Selected USB Device Tree

Shows the file structure of the selected USB drive for user inspection.

### Scan Type Selection

Allows users to choose between different types of scans (quick scan, full scan, etc.).

### Scanning Process

Thoroughly checks the USB drive for malware and other threats.

### Display Infected Files

Lists detected threats and provides options for handling them.

## Installation

## Compatibility

USBVacuum has been tested and is only supported on Debian 12.

### Requirements

- Python 3
- Docker
- Other dependencies listed in `install_dependencies.sh`

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/USBVacuum.git
    cd USBVacuum
    ```

2. Install dependencies:
    ```bash
    ./install_dependencies.sh
    ```

4. Restart the system to apply changes

3. Start the software:
    ```bash
    ./start.sh
    ```

## Usage

To use USBVacuum, follow these steps:

1. Insert the USB drive into the system. Make sure the drive is mounted correctly.

2. Launch the USBVacuum application.

3. Select the USB drive from the list of detected devices.

4. Choose the type of scan you want to perform (quick scan, full scan, etc.).

5. Start the scan and wait for the process to complete.

6. Review the scan results

7. Your USB drive is now clean and safe to use.

## Future Improvements

- Integration with cloud-based threat intelligence for real-time updates.
- Transfer files to new storage
- Enhanced user interface with more customization options.
- Support for additional languages and platforms.

## Customization and Notes

- Future Figma integration for UI/UX design

## IMPORTANT

- We cannot guarantee the complete removal of all malware. The software is designed to detect and remove known threats, but new and emerging malware may not be detected. In addition, some malware may be embedded in the firmware of the USB drive, making it impossible to remove without specialized tools.
- There is only one scan engine available in the current version of the software. Future versions may include additional scan engines for improved detection rates.
- The software is provided as-is, without any warranty or guarantee of performance. Use at your own risk.
- The software is intended for educational and informational purposes only. It is not a substitute for professional security tools and practices.

## Credits

- Tkinter-Designer : https://github.com/ParthJadhav/Tkinter-Designer
- Figma : https://www.figma.com/
- Docker : https://www.docker.com/
- Python.org : https://www.python.org/
- Visual Studio Code : https://code.visualstudio.com/
- ClamAV : https://www.clamav.net/
