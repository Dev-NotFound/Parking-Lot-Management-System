import time

MAX_SPOTS = 10

class Car:
    def __init__(self, license_plate, spot_number=-1):
        self.license_plate = license_plate
        self.arrival_time = time.ctime() 
        self.spot_number = spot_number

class ParkingLotSystem:
    def __init__(self):
        
        self.parking_lot_stack = []
        
        self.waiting_list_queue = []
        
        self.parked_spots = [0] * MAX_SPOTS

    def find_empty_spot(self):
        
        for i in range(MAX_SPOTS):
            if self.parked_spots[i] == 0:
                return i + 1
        return -1

    def park_car(self, plate):
        """Adds a car to the lot or waiting list[cite: 18, 41]."""
        new_car = Car(plate)
        spot = self.find_empty_spot()

        if spot != -1:
            new_car.spot_number = spot
            self.parked_spots[spot - 1] = 1
            self.parking_lot_stack.append(new_car) # push operation
            print(f"✅ Car {plate} parked at spot {spot}.")
        else:
            self.waiting_list_queue.append(new_car) # enqueue operation
            print(f"⚠️ Parking full! {plate} added to waiting queue.")

    def remove_car(self, spot_number):
        """Removes a specific car and moves the next waiting car in[cite: 43]."""
        if spot_number < 1 or spot_number > MAX_SPOTS:
            print("❌ Invalid spot number.")
            return

        if self.parked_spots[spot_number - 1] == 0:
            print(f"❌ Spot {spot_number} is already empty.")
            return

        # Logic to remove specific spot from stack
        temp_stack = []
        target_car = None

        while self.parking_lot_stack:
            car = self.parking_lot_stack.pop()
            if car.spot_number == spot_number:
                target_car = car
                break
            else:
                temp_stack.append(car)

        
        while temp_stack:
            self.parking_lot_stack.append(temp_stack.pop())

        if target_car:
            self.parked_spots[spot_number - 1] = 0
            print(f"🚗 Car {target_car.license_plate} removed from spot {spot_number}.")
            
           
            if self.waiting_list_queue:
                waiting_car = self.waiting_list_queue.pop(0) 
                waiting_car.spot_number = spot_number
                self.parked_spots[spot_number - 1] = 1
                self.parking_lot_stack.append(waiting_car)
                print(f"🅿️ Waiting car {waiting_car.license_plate} now parked at spot {spot_number}.")

    def display_status(self):
        """Displays current parking and queue status[cite: 39, 44]."""
        print("\n--- Parking Lot Status ---")
        if not self.parking_lot_stack:
            print("Parking lot is empty.")
        for car in self.parking_lot_stack:
            print(f"Spot {car.spot_number}: {car.license_plate} (Arrived: {car.arrival_time})")
        
        print("\n--- Waiting Queue ---")
        if not self.waiting_list_queue:
            print("No cars waiting.")
        for car in self.waiting_list_queue:
            print(f"Waiting: {car.license_plate}")

# Main Menu Logic
def main():
    system = ParkingLotSystem()
    while True:
        print("\n1. Park Car  2. Remove Car  3. View Status  4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            plate = input("Enter License Plate: ")
            system.park_car(plate)
        elif choice == '2':
            spot = int(input("Enter Spot Number to clear: "))
            system.remove_car(spot)
        elif choice == '3':
            system.display_status()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()