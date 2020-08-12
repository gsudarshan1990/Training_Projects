"""
This is an example of the class
"""

#Imagine you're writing an exercise-tracking app like Fitbit
#or MyFitnessPal. Part of your app is that a user can log an
#exercise session by naming the exercise, the intensity, and
#the duration.
#
#Write a class called ExerciseSession. ExerciseSession
#should have a constructor that requires two strings and an
#integer: the strings represent the exercise name and the
#exercise intensity, which will be "Low", "Moderate", or
#"High". The integer will represent the length of the
#exercise session in minutes. These should be saved in the
#instance of the class.
#
#Then, add three getters to the class. The getters should
#be named get_exercise, get_intensity, and get_duration,
#and should return the exercise string, the exercise
#intensity, and the duration, respectively.
#
#The setters should be named set_exercise, set_intensity,
#and set_duration. Each should have one parameter (besides
#self), which should be stored as the new value of
#exercise, intensity, or duration. You may assume only
#valid values will be passed in.

#Add a new method to that class called calories_burned.
#calories_burned should have no parameters (besides self, as
#every method in a class has). It should return an integer
#representing the number of calories burned according to the
#following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Moderate", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.


class ExerciseSession:
    """This represents the Exercise Session"""
    def __init__(self, exercise_name, exercise_intensity, exercise_duration):
        """This is used to initialize the values"""
        self.exercise_name = exercise_name
        self.exercise_intensity = exercise_intensity
        self.duration = exercise_duration

    def get_exercise(self):
        """This provides the name of the exercise event"""
        return self.exercise_name

    def get_intensity(self):
        """This provides the intensity of the exercise event like high, medium and low"""
        return self.exercise_intensity

    def get_duration(self):
        """This provides the duration of the exercise"""
        return self.duration

    def set_exercise(self, newname):
        """This is used to the set the exercise name"""
        print('Exercise name is changed from ', self.exercise_name,"to", newname)
        self.exercise_name = newname

    def set_intensity(self, newintensity):
        """This is used to set the exercise intensity"""
        print('Exercise intensity is changed from ', self.exercise_intensity, "to", newintensity)
        self.exercise_intensity = newintensity

    def set_duration(self, newduration):
        """This is used to set the exercise duration"""
        print('The duration is changed from', self.duration, "to", newduration)
        self.duration = newduration

    def calories_burned(self):
        """This is used to define the number of the calories burned"""
        if self.exercise_intensity == "Low":
            return 4*self.duration
        elif self.exercise_intensity == "Moderate":
            return 8*self.duration
        elif self.exercise_intensity == "High":
            return 12*self.duration

new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
print(new_exercise.calories_burned())