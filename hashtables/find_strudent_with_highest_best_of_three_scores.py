import heapq
def find_student_with_highest_best_of_three_scores(names_score_data):
    student_with_max_score, max_score = None, 0
    student_scores = {}
    for line in names_score_data :
        name, score = line.split(" ")
        if not name in student_scores :
            student_scores[name] = [1, [score]]
        else:
            if student_scores[name][0] < 3 :
                student_scores[name][0] += 1
                heapq.heappush(student_scores[name][1], score)
            else:
                heapq.heappushpop(student_scores[name][1], score)
        if student_scores[name][0] == 3 :
            avg_score = sum(student_scores[name][1])/3
            if avg_score > max_score :
                max_score, student_with_max_score = avg_score, name
    return (student_with_max_score, max_score)

