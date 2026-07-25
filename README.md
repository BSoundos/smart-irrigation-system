# Smart Irrigation System 🌱💧

An IoT-based automated plant watering system that combines a Flutter mobile application with Raspberry Pi hardware to provide intelligent irrigation control. The system supports multiple watering modes and real-time sensor monitoring.

## 🎯 Features

### Mobile Application
- **User Authentication**: Secure login, registration, and password reset via Firebase
- **Multiple Irrigation Modes**:
  - **Manual Mode**: Instant watering control
  - **Automatic Mode**: Soil moisture-based automatic watering
  - **Programmed Mode**: Scheduled watering by day and time
- **Real-time Monitoring**: Live temperature, humidity, and soil moisture data
- **User Profiles**: Personalized user settings and preferences
- **Modern UI**: Curved navigation bar, custom icons, and smooth animations

### Hardware System
- **Sensor Integration**:
  - DHT22 temperature and humidity sensor
  - Soil moisture sensor (via Arduino)
  - Water level monitoring
- **Actuator Control**: GPIO-based water pump control
- **Firebase Integration**: Real-time data synchronization

### Main components:
- **mobile_app/** - Flutter mobile application with authentication, irrigation controls, and real-time monitoring
- **hardware/** - Raspberry Pi and Arduino code for sensor integration and actuator control
- **docs/** - Installation guides and user manuals

## 🛠️ Tech Stack

### Mobile App
- **Framework**: Flutter (Dart SDK >=2.12.0 <3.0.0)
- **Backend**: Firebase (Auth, Firestore, Analytics)

### Hardware
- **Platform**: Raspberry Pi 4
- **Language**: Python 3
- **Sensors**: DHT22, Soil Moisture Sensor
- **Communication**: Serial (UART), GPIO
- **Cloud**: Firebase Admin SDK

## 👥 Team

This project was developed by a team of 6 students in 2021-2022:
- **Asma Sebah & Yasmine Belmellat** - UI/UX design and home screens
- **Salma Taib & Selma Zerrouki** - Flutter App developpment
- **Soundos Benni & Hind Ledra** - Hardware integration and testing

## 📄 License

This project is provided as-is for educational purposes.

## 📞 Support

For installation guides and user manuals, refer to the PDF documentation in the `docs/` folder.

## 🎥 Demo Videos

Demo videos showcasing the system functionality are available. See [demo-videos.md](demo-videos.md) for detailed demonstrations of the irrigation modes and hardware setup.


