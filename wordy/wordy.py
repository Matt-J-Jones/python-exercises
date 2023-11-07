import operator
def answer(question):
    operators_dict = {
        'plus': operator.add,
        'minus': operator.sub,
        'multiplied': operator.mul,
        'divided': operator.truediv
    }
    cleaned_question = question.replace("What is ", "")
    cleaned_question = cleaned_question.replace("What is", "")
    cleaned_question = cleaned_question.replace("?", "")
    cleaned_question = cleaned_question.replace("by", "")
    cleaned_question = cleaned_question.split()
    question_length = len(cleaned_question)

    if cleaned_question == []:
        raise ValueError("syntax error")
    if len(cleaned_question) == 1:
        return int(cleaned_question[0])
    if cleaned_question[0] in operators_dict or cleaned_question[-1] in operators_dict:
        raise ValueError("syntax error")
    if cleaned_question[1] not in operators_dict and not cleaned_question[1].isdigit():
        raise ValueError("unknown operation")
    if cleaned_question[1] not in operators_dict or cleaned_question[2] in operators_dict:
        raise ValueError("syntax error")
    if cleaned_question[-1].isdigit() and cleaned_question[-2].isdigit():
        raise ValueError("syntax error")
    if question_length == 3:
        x = int(cleaned_question[0])
        y = int(cleaned_question[2])
        return operators_dict[cleaned_question[1]](x, y)
    if question_length == 5:
        x = operators_dict[cleaned_question[1]](int(cleaned_question[0]), int(cleaned_question[2]))
        y = int(cleaned_question[4])
        return operators_dict[cleaned_question[3]](x,y)
