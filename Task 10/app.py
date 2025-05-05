from flask import Flask, render_template, request

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "assalam-o-alaikum" in user_input or "aoa" in user_input:
        return "Hello! How can I assist you with your admission inquiries today?"

    elif "admission" in user_input:
        return "Admissions are open from July to September. Apply online at our university website."
    elif "programs" in user_input or "courses" in user_input:
        return "We offer undergraduate and postgraduate programs in Engineering, Computer Science, Artificial Intelligence, Software Engineering"
    elif "fee" in user_input or "tuition" in user_input:
        return "The fee structure varies by program. For an undergraduate program, it's approximately PKR 175,000 per semester."
    elif "contact" in user_input:
        return "You can contact the admission office at admissions@university.edu or call 03077774244"
    elif "scholarships" in user_input:
        return "We offer merit-based scholarships for high-performing students. You can apply during the admission process."
    elif "campus" in user_input or "facilities" in user_input:
        return "Our campus has state-of-the-art facilities including libraries, computer labs, a sports complex, and student lounges."
    elif "ranking" in user_input or "university ranking" in user_input:
        return "We are ranked among the top 10 universities in Pakistan for Engineering and Computer Science."
    elif "eligibility" in user_input or "requirements" in user_input:
        return "For undergraduate programs, you need at least 60% marks in your intermediate exams or equivalent. For postgraduate programs, a relevant Bachelor's degree is required."
    elif "deadline" in user_input:
        return "The application deadline for undergraduate admissions is September 30th, and for postgraduate, it's October 15th."
    
    else:
        return "I'm not sure how to help with that. You can ask about admissions, programs, scholarships, fees, contact info, or campus facilities."

@app.route("/", methods=["GET", "POST"])
def index():
    chat = []
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_response(user_input)
        chat.append(("You", user_input))
        chat.append(("Bot", response))
    return render_template("index.html", chat=chat)

if __name__ == "__main__":
    app.run(debug=True)
