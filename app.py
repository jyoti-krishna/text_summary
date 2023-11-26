from flask import Flask, render_template,request
from text_summary import summarizer

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])

def result():
    if request.method=='POST':
        text=request.form['text']
        summary, doc, len_summ, len_org= summarizer(text)
    return render_template('summary.html',summary=summary,doc=doc, len_summ=len_summ,len_org=len_org)

if __name__=="__main__":
    app.run(debug=True)