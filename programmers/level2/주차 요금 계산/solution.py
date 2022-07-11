from math import ceil


def solution(fees, records):
    default_time, default_cost, unit_time, unit_cost = fees
    cars = {car_num.split()[1]: [] for car_num in records}
    fares = []

    for record in records:
        time, car_num, status = record.split()
        hour, minute = map(int, time.split(':'))
        cars[car_num].append(hour*60 + minute)

    for car, record in sorted(cars.items()):
        total_time = 0
        if len(cars[car]) % 2 != 0:
            cars[car].append(23*60 + 59)
        for i in range(0, len(record), 2):
            in_time, out_time = record[i], record[i+1]
            total_time += out_time - in_time

        if total_time <= default_time:
            fares.append(default_cost)
        else:
            fares.append(default_cost + ceil((total_time - default_time) / unit_time) * unit_cost)

    return fares


if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
               "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))
