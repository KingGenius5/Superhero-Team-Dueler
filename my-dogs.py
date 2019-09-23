from dog import Dog#cleans things up a bit so that you
#don't call from do within each of your functions
#each time

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
my_other_dog.bark()

my_third_dog = Dog("Clifford", "BigBoy")
my_third_dog.bark()

Dog.greeting = "Woah"
