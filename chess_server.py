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
        crash_test = crash_test
    except:
        print("Error: didn't receive json correctly")
        return "Error: didn't receive json correctly", 404
    #------------------------------#

    old_board = cc.Board(boards_json[0],"old")
    new_board = cc.Board(boards_json[1],"new")

    changes = cc.Board.change_detector(old_board,new_board)
    if changes == False:
        return "error: bad move", 404
    
    try:
        soldier_val, cell_dict = cc.Board.who_moved(old_board,new_board,changes)
    except TypeError:
        return "error: bad move", 404
        
    if soldier_val == False:
        return "error: bad move", 404
    
    soldier = cc.Soldier(soldier_val, cell_dict["old"], cell_dict["new"])

    print1 = str(soldier.Type.name) + "\n" + str(soldier.Color.name) + "\n" + str(soldier.old_cell) + "\n" + str(soldier.new_cell) 
    return print1 


if __name__ == "__main__":
    app.run(debug=True, port=5000)