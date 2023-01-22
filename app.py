import gradio as gr
import pandas as pd
import os
csvfile = '수학(상)_테스트_000_정답.csv'
df = pd.read_csv(csvfile)

filename = os.path.basename(csvfile)[:-7]
filedir = os.path.dirname(csvfile)

rignt_answer_list = df['정답']
jumsu = df['배점']
question_number = len(rignt_answer_list)
print(rignt_answer_list)

def submit(*arg):
    global stu_answer_list, incorrect1
    stu_answer_list = arg
    print(stu_answer_list)
    incorrect1 = []

    sum = 0
    incorrect = []
    output={}
    for i in range(0, len(rignt_answer_list)):
        if int(rignt_answer_list[i]) == int(stu_answer_list[i]):
            sum = sum + jumsu[i]
        else:
            incorrect.append(i)   #틀린 문항 번호추가
        
    for i in range(0, len(incorrect)):
        incorrect1.append(incorrect[i]+1)
        
    output = {'시험명':[filename], '점수':[sum], '틀린문항':[incorrect1]}

    outputcsv = pd.DataFrame(output)
    if not os.path.exists(filedir+'/'+'result.csv'):
        outputcsv.to_csv(filedir+'/'+'result.csv',index=False, mode='w', encoding='utf-8-sig')
    else:
        outputcsv.to_csv(filedir+'/'+'result.csv',index=False, mode='a', encoding='utf-8-sig', header=False)

    # print('점수는'+sum+', 틀린 문항은 '+incorrect1+'번 입니다.')
    return '점수는'+str(sum)+', 틀린 문항은 '+str(incorrect1)+'번 입니다.'














    
def cancel(bb):
    pass

stu_list=[('김성정', '1111'), ('박핑코', '1234'), ('박토순', '1234'), ('박흑코', '1234')]
with gr.Blocks() as test:
    gr.Markdown(f'{filename} : 학생 답안 제출기')
    
    rr=list(range(question_number))
    
    for i in range(question_number):
        if rignt_answer_list[i] not in [1,2,3,4,5]:
            rr[i] = gr.Textbox(label=str(i+1)+'번 문항의 정답을 입력하세요')
        else:
            rr[i]=gr.Radio(['1','2','3','4','5'], label=str(i+1)+'번 문항의 정답을 입력하세요')
    with gr.Row():
        btn1 = gr.Button('제출')
        btn2 = gr.Button('취소')
    txt_result = gr.Textbox(value='', label='시험결과')
    btn1.click(submit, inputs=[rr[i] for i in range(0,question_number)], outputs=txt_result)


# btn2.click(cancel, inputs=)gr.Radio(['1','2','3','4','5'], label=str(i+1)+'번 문항의 정답을 입력하세요')
# test.launch()  #
test.launch(auth=stu_list, share=True)  #