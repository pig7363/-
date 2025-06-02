from const import SCORE_GRADES


class Grading:
    def __init__(self, raw_score):
        self.raw_score = raw_score
    pass

# 표준점수 = (원점수 - 평균) / 표준편차
    def get_z_score(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev
        return (self.raw_score - self.mean) / self.std_dev
    
# 학점계산
    def get_grade(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev
        z_score = self.get_z_score()
        if z_score >= 3:
            z_score = 3
        elif z_score >= 2:
            z_score = 2
        elif z_score >= 1:
            z_score = 1
        elif z_score >= 0:
            z_score = 0
        elif z_score >= -1:
            z_score = -1
        elif z_score >= -2:
            z_score = -2
        elif z_score >= -3:
            z_score = -3
        else:
            z_score = -4
            return SCORE_GRADES[z_score]
