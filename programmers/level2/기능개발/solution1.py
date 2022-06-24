def solution(progresses, speeds):
    answer = []
    for i, work in enumerate(zip(progresses, speeds)):
        progress, speed = work
        took = 0
        for _ in range(progress, 100, speed):
            took += 1

        if took == 0:
            continue

        for j in range(i, len(progresses)):
            progresses[j] += speeds[j] * took

        done = 0
        for j in range(i, len(progresses)):
            if progresses[j] < 100:
                break
            done += 1

        answer.append(done)

    return answer


if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))
