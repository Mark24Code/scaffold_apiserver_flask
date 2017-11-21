from util.random_talk import RandomTalk


random_talk = RandomTalk()

sample_data = []

for i in range(10):
    one_data = {}
    one_data[random_talk.randomName(5)]={
        "name":random_talk.randomName(5),
        "age":random_talk.randomAge(2),
        "id":random_talk.randomCode(11)
    }
    sample_data.append(one_data)
