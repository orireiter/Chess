from flask import Flask, request, jsonify
from flask_cors import CORS
import chess_classes as cc


#------------------------------------------------------------------#
# FLASK related

#-------------------------------------------------#
# creating app
app = Flask(__name__)
# allowing different origins to communicate with this server
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#-------------------------------------------------#

#-------------------------------------------------#
@app.route("/board_check", methods=["POST"])
def board_check():
    #------------------------------#
    # json related
    try:
        boards_json = request.get_json()
    # It's put in try/except to make sure it doesn't crash.
    # And also doesn't proceed without a json.
        # a test to see if I can do list actions
        crash_test = boards_json[0]
    except:
        print("Error: didn't receive json correctly")
        return "Error: didn't receive json correctly", 404
    #------------------------------#

    old_board = cc.Board(boards_json[0],"old")
    new_board = cc.Board(boards_json[1],"new")

    print(f"old board: \n{old_board.getBoard()}")
    print(f"new board: \n{new_board.getBoard()}")
    return str(new_board.getColumn(2))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)