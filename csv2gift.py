if __name__ == "__main__":
    delimiter = ','
    csv_file = 'test.csv'
    gift_file = csv_file.replace('csv', 'txt')
    if '.txt' not in gift_file:
        gift_file = gift_file + '.txt'

    with open(csv_file, 'r') as csv:
        questions = csv.readlines()

    gift_questions = []
    for q in questions:
        q = q.replace('\n', '')
        qparts = q.split(delimiter)
        gift_qparts = []
        gift_qparts.append('::' + qparts[0])
        gift_qparts.append('::%s {' % (qparts[1]))
        gift_qparts.append('=' + qparts[2])
        for qp in qparts[3:]:
            gift_qparts.append('~' + qp)
        gift_qparts.append('}\n\n')
        gift_questions.append('\n'.join(gift_qparts))

    with open(gift_file, 'w') as gift:
        gift.writelines(gift_questions)
