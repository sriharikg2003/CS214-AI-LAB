
/*
 * @file botTemplate.cpp
 * @author Arun Tejasvi Chaganty <arunchaganty@gmail.com>
 * @date 2010-02-04
 * Template for users to create their own bots
 */

#include "Othello.h"
#include "OthelloBoard.h"
#include "OthelloPlayer.h"
#include <cstdlib>
using namespace std;
using namespace Desdemona;

class MyBot : public OthelloPlayer
{
public:
    MyBot(Turn turn);

    virtual Move play(const OthelloBoard &board);
    virtual int minimax(const OthelloBoard &board, int depth, bool MaxPlayer);

private:
};

MyBot::MyBot(Turn turn)
    : OthelloPlayer(turn)
{
}

Move MyBot::play(const OthelloBoard &board)
{

    list<Move> moves = board.getValidMoves(turn);

    int MaxValue = -20000;

    Move &best_move = moves.front();
    list<Move>::iterator it;

    for (it = moves.begin(); it != moves.end(); it++)
    {
        OthelloBoard new_Board = board;
        new_Board.makeMove(turn, *it);

        // Once the max player has moved , now it is min players turn so bool Maxplayer = False
        int value = minimax(new_Board, 4, false);

        if (value > MaxValue)
        {
            MaxValue = value;
            best_move = *it;
        }
    }
    // printf("Selecting move : (%d, %d)\n", best_move.x, best_move.y);
    board.print();

    return best_move;
}

int MyBot::minimax(const OthelloBoard &board, int depth, bool MaxPlayer)
{

    if (depth == 0)
    {
        // At the terminals we will send the heuritic value
        int send;
        int heur = 3;
        switch (heur)
        {
        case 1:
        {
            // Good heuristic
            send = board.getBlackCount() - board.getRedCount();
            switch (turn)
            {
            // If its black's turn send the B-R values
            case BLACK:
                return send;
            // If it is red's turn send the R-B value
            case RED:
                return (-1) * send;
            }
        }

        case 2: // not so good heuristic
        {
            int opp_value = board.getValidMoves(RED).size();
            int my_value = board.getValidMoves(BLACK).size();
            send = my_value - opp_value;

            switch (turn)
            {
            // If its black's turn send the B-R values
            case BLACK:
                return send;
            // If it is red's turn send the R-B value
            case RED:
                return (-1) * send;
            default:
                return 1;
            }
        }

        case 3: // very nice heuristic
        {

            int MyValue = 0;
            int OppValue = 0;

            int A[] = {0, 0, 7, 7};
            int B[] = {0, 7, 0, 7};
            // Corner value adds more

            for (int i = 0; i < 4; ++i)
            {
                if (board.get(A[i], B[i]) == this->turn)
                    MyValue += 2000;
                else if (board.get(A[i], B[i]) == other(this->turn))
                    OppValue += 2000;
            }
            // just diagonal to corner penalized high

            int C[] = {1, 0, 7, 1, 0, 6, 6, 7};
            int D[] = {0, 1, 1, 7, 6, 0, 7, 6};

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(C[i], D[i]) == this->turn)
                    MyValue -= 1000;
                else if (board.get(C[i], D[i]) == other(this->turn))
                    OppValue -= 1000;
            }

            // Outline edges valued high

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(i, 0) == this->turn)
                    MyValue += 350;
                if (board.get(i, 7) == this->turn)
                    MyValue += 350;
                if (board.get(0, i) == this->turn)
                    MyValue += 350;
                if (board.get(7, i) == this->turn)
                    MyValue += 350;

                if (board.get(i, 0) == other(this->turn))
                    OppValue += 350;
                if (board.get(i, 7) == other(this->turn))
                    OppValue += 350;
                if (board.get(0, i) == other(this->turn))
                    OppValue += 350;
                if (board.get(7, i) == other(this->turn))
                    OppValue += 350;
            }

            return (MyValue - OppValue);
        }

        default:
            return 1;
        }
    }

    if (MaxPlayer)
    {
        // For the max player , recursively find the Max Value
        int MaxValue = -20000;
        // moves contains the address of the valid moves from current state of the max player
        list<Move> moves = board.getValidMoves(turn);

        // it points to the iterator over the moves
        list<Move>::iterator it;

        for (it = moves.begin(); it != moves.end(); it++)
        {
            // each time new_Board is assigned to board passed initally
            OthelloBoard new_Board = board;

            // Move is virtually made by the Max player
            new_Board.makeMove(turn, *it);

            // Maxvalue is assigned to be max of values of its child nodes from minimax algorithm recursively

            // Given limitation over depth , depth value decreases by one
            // when depth zero , heuristic is returned
            // Next player is MinPlayer os bool MaxPlayer = False

            MaxValue = max(minimax(new_Board, depth - 1, false), MaxValue);
        }
        return MaxValue;
    }
    else
    {
        // Min player turn
        int min_value = 20000;

        // moves contains pointers to valid moves that Min Player can take
        list<Move> moves = board.getValidMoves(other(turn));

        list<Move>::iterator it;

        for (it = moves.begin(); it != moves.end(); it++)
        {
            OthelloBoard new_Board = board;
            new_Board.makeMove(other(turn), *it);
            // Min value is assigned to Min Node
            // Next player is MaxPlayer os bool MaxPlayer = True
            min_value = min(minimax(new_Board, depth - 1, true), min_value);
        }
        return min_value;
    }
};

// The following lines are _very_ important to create a bot module for Desdemona

extern "C"
{
    OthelloPlayer *createBot(Turn turn)
    {
        return new MyBot(turn);
    }

    void destroyBot(OthelloPlayer *bot)
    {
        delete bot;
    }
}
