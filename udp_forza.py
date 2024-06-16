#Made By Jake

import socket
import struct

UDP_IP = "0.0.0.0"
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def recive_udp(allow_vebosity=True):
    if allow_vebosity:
        print("\n")
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    if allow_vebosity:
        print(f"received message: {addr}")
    
    expected_length = 332  # Expected length based on documentation.. probably

    # Check if the received data length matches the expected length
    if len(data) < expected_length:
        if allow_vebosity:
            print(f"Unexpected data length: {len(data)}, padding data.")
        data = data.ljust(expected_length, b'\0')
    elif len(data) > expected_length:
        if allow_vebosity:
            print(f"Unexpected data length: {len(data)}, truncating data.")
        data = data[:expected_length]

    # Define the structure format based on the documentation (Dumbest, and useless Documentation)
    format_string = (
        "iI"   # IsRaceOn, TimestampMS
        "fff"  # EngineMaxRpm, EngineIdleRpm, CurrentEngineRpm
        "fff"  # AccelerationX, AccelerationY, AccelerationZ
        "fff"  # VelocityX, VelocityY, VelocityZ
        "fff"  # AngularVelocityX, AngularVelocityY, AngularVelocityZ
        "fff"  # Yaw, Pitch, Roll
        "ffff" # NormalizedSuspensionTravelFrontLeft, NormalizedSuspensionTravelFrontRight, NormalizedSuspensionTravelRearLeft, NormalizedSuspensionTravelRearRight
        "ffff" # TireSlipRatioFrontLeft, TireSlipRatioFrontRight, TireSlipRatioRearLeft, TireSlipRatioRearRight
        "ffff" # WheelRotationSpeedFrontLeft, WheelRotationSpeedFrontRight, WheelRotationSpeedRearLeft, WheelRotationSpeedRearRight
        "iiii" # WheelOnRumbleStripFrontLeft, WheelOnRumbleStripFrontRight, WheelOnRumbleStripRearLeft, WheelOnRumbleStripRearRight
        "ffff" # WheelInPuddleDepthFrontLeft, WheelInPuddleDepthFrontRight, WheelInPuddleDepthRearLeft, WheelInPuddleDepthRearRight
        "ffff" # SurfaceRumbleFrontLeft, SurfaceRumbleFrontRight, SurfaceRumbleRearLeft, SurfaceRumbleRearRight
        "ffff" # TireSlipAngleFrontLeft, TireSlipAngleFrontRight, TireSlipAngleRearLeft, TireSlipAngleRearRight
        "ffff" # TireCombinedSlipFrontLeft, TireCombinedSlipFrontRight, TireCombinedSlipRearLeft, TireCombinedSlipRearRight
        "ffff" # SuspensionTravelMetersFrontLeft, SuspensionTravelMetersFrontRight, SuspensionTravelMetersRearLeft, SuspensionTravelMetersRearRight
        "i"    # CarOrdinal
        "i"    # CarClass
        "i"    # CarPerformanceIndex
        "i"    # DrivetrainType
        "i"    # NumCylinders
        "fff"  # PositionX, PositionY, PositionZ
        "f"    # Speed
        "f"    # Power
        "f"    # Torque
        "ffff" # TireTempFrontLeft, TireTempFrontRight, TireTempRearLeft, TireTempRearRight
        "f"    # Boost
        "f"    # Fuel
        "f"    # DistanceTraveled
        "f"    # BestLap
        "f"    # LastLap
        "f"    # CurrentLap
        "f"    # CurrentRaceTime
        "H"    # LapNumber
        "B"    # RacePosition
        "B"    # Accel
        "B"    # Brake
        "B"    # Clutch
        "B"    # HandBrake
        "B"    # Gear
        "b"    # Steer
        "b"    # NormalizedDrivingLine
        "b"    # NormalizedAIBrakeDifference
        "ffff" # TireWearFrontLeft, TireWearFrontRight, TireWearRearLeft, TireWearRearRight
        "i"    # TrackOrdinal
    )
    
    try:
        # Unpack the data according to the format string
        unpacked_data = struct.unpack(format_string, data)
    except struct.error as e:
        if allow_vebosity:
            print(f"Error unpacking data: {e}")
        
    return unpacked_data

    # Print the unpacked data for debugging
    # print(unpacked_data)
    
    # is_race_on = unpacked_data[0]
    # gear = unpacked_data[81]
    # Current_lap = unpacked_data[73]
    # # ... and so on for other fields
    # print(f"IsRaceOn: {is_race_on}, Gear: {gear}, Current Lap: {Current_lap}")

# Index | Field Name
# ------|------------------------------
#   0   | IsRaceOn
#   1   | TimestampMS
#   2   | EngineMaxRpm
#   3   | EngineIdleRpm
#   4   | CurrentEngineRpm
#   5   | AccelerationX
#   6   | AccelerationY
#   7   | AccelerationZ
#   8   | VelocityX
#   9   | VelocityY
#   10  | VelocityZ
#   11  | AngularVelocityX
#   12  | AngularVelocityY
#   13  | AngularVelocityZ
#   14  | Yaw
#   15  | Pitch
#   16  | Roll
#   17  | NormalizedSuspensionTravelFrontLeft
#   18  | NormalizedSuspensionTravelFrontRight
#   19  | NormalizedSuspensionTravelRearLeft
#   20  | NormalizedSuspensionTravelRearRight
#   21  | TireSlipRatioFrontLeft
#   22  | TireSlipRatioFrontRight
#   23  | TireSlipRatioRearLeft
#   24  | TireSlipRatioRearRight
#   25  | WheelRotationSpeedFrontLeft
#   26  | WheelRotationSpeedFrontRight
#   27  | WheelRotationSpeedRearLeft
#   28  | WheelRotationSpeedRearRight
#   29  | WheelOnRumbleStripFrontLeft
#   30  | WheelOnRumbleStripFrontRight
#   31  | WheelOnRumbleStripRearLeft
#   32  | WheelOnRumbleStripRearRight
#   33  | WheelInPuddleDepthFrontLeft
#   34  | WheelInPuddleDepthFrontRight
#   35  | WheelInPuddleDepthRearLeft
#   36  | WheelInPuddleDepthRearRight
#   37  | SurfaceRumbleFrontLeft
#   38  | SurfaceRumbleFrontRight
#   39  | SurfaceRumbleRearLeft
#   40  | SurfaceRumbleRearRight
#   41  | TireSlipAngleFrontLeft
#   42  | TireSlipAngleFrontRight
#   43  | TireSlipAngleRearLeft
#   44  | TireSlipAngleRearRight
#   45  | TireCombinedSlipFrontLeft
#   46  | TireCombinedSlipFrontRight
#   47  | TireCombinedSlipRearLeft
#   48  | TireCombinedSlipRearRight
#   49  | SuspensionTravelMetersFrontLeft
#   50  | SuspensionTravelMetersFrontRight
#   51  | SuspensionTravelMetersRearLeft
#   52  | SuspensionTravelMetersRearRight
#   53  | CarOrdinal
#   54  | CarClass
#   55  | CarPerformanceIndex
#   56  | DrivetrainType
#   57  | NumCylinders
#   58  | PositionX
#   59  | PositionY
#   60  | PositionZ
#   61  | Speed
#   62  | Power
#   63  | Torque
#   64  | TireTempFrontLeft
#   65  | TireTempFrontRight
#   66  | TireTempRearLeft
#   67  | TireTempRearRight
#   68  | Boost
#   69  | Fuel
#   70  | DistanceTraveled
#   71  | BestLap
#   72  | LastLap
#   73  | CurrentLap
#   74  | CurrentRaceTime
#   75  | LapNumber
#   76  | RacePosition
#   77  | Accel
#   78  | Brake
#   79  | Clutch
#   80  | HandBrake
#   81  | Gear
#   82  | Steer
#   83  | NormalizedDrivingLine
#   84  | NormalizedAIBrakeDifference
#   85  | TireWearFrontLeft
#   86  | TireWearFrontRight
#   87  | TireWearRearLeft
#   88  | TireWearRearRight
#   89  | TrackOrdinal

