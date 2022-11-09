import pickle

with open('teacher_info.pickle', 'wb') as usr_file:
    teacher_info = {'teacher':'teacher','2':'2'}
    pickle.dump(teacher_info, usr_file)