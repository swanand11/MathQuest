from sympy import symbols, Eq, solve,S
import random
class Boss:
    def __init__(self, topic):
        self.topic = topic

    def get_problem(self):
        x, y = symbols('x y')
        a1, b1, c1 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        a2, b2, c2 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        eq1 = Eq(a1*x + b1*y, c1)
        eq2 = Eq(a2*x + b2*y, c2)
        problem = f"Solve the system of equations:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}"
        solutions = solve((eq1, eq2), (x, y))
        answer = [round(float(solutions[x]), 4), round(float(solutions[y]), 4)]
        return problem, answer

class BossBattle:
    def __init__(self, boss):
        self.boss = boss

    def fight(self):
        print(f"Facing Boss on {self.boss.topic}")
        problem, correct_answer = self.boss.get_problem()
        if correct_answer is None:
            print("No problem to solve.")
            return

        print(problem)
        hp_user = 100
        hp_boss = 100

        while hp_user > 0 and hp_boss > 0:
            answer = input("Enter your answer as a list of two numerical values (e.g., [2.5, 3.0]): ")
            try:
                answer_list = answer.strip("[]").split(",")
                user_x, user_y = map(float, [ans.strip() for ans in answer_list])
            except (ValueError, IndexError):
                print("Invalid input. Please enter your answers as a list of two numerical values (e.g., [2.5, 3.0]).")
                continue

            # Allowing for some tolerance in floating-point comparisons
            tolerance = 0.0001
            if abs(user_x - correct_answer[0]) < tolerance and abs(user_y - correct_answer[1]) < tolerance:
                hp_boss -= 25
                print("Correct! Boss's HP reduced.")
                problem, correct_answer = self.boss.get_problem()
                if hp_boss <= 0:
                    print("You have won the battle!")
                    break
                problem, correct_answer = self.boss.get_problem()
            else:
                hp_user -= 25
                print(f"Incorrect! Your HP reduced")

            print(f"Your HP: {hp_user}, Boss's HP: {hp_boss}")
            if hp_user <= 0:
                print(f"You lost. The correct answer was: {correct_answer}. Try again!")
                break
            print(problem)
