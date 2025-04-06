import model.note

def write_file(array, mode):
    file = open("notes.csv", mode = 'w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.cdv", mode = mode, encoding='utf-8')
    for notes in array:
        file.write(model.note.note.to_string(notes))
        file.write('\n')
    file.close