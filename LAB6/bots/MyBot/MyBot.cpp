
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



class MyBot: public OthelloPlayer
{
    public:
    
        

        MyBot( Turn turn );


        virtual Move play( const OthelloBoard& board );
        virtual int minimax( const OthelloBoard& board, int depth, bool MaxPlayer);
    private:
};


MyBot::MyBot( Turn turn )
    : OthelloPlayer( turn )
{
}

int MyBot::minimax( const OthelloBoard& board, int depth, bool MaxPlayer )
{
    // We have set depth to 4 in this code
        // if ( depth == 0 )
        // {
        //     // At the terminals we will send the heuritic value 
        //     int send  = board.getBlackCount() - board.getRedCount();;
        //         switch(turn)
        //         {
        //             // If its black's turn send the B-R values
        //             case BLACK:
        //                 return send;
        //             // If it is red's turn send the R-B value
        //             case RED:
        //                 return (-1)*send;
        //         }
        // }

        // if ( MaxPlayer )
        // {
        //     // For the max player , recursively find the Max Vla
        //     int MaxValue = -20000;
        //     list<Move> moves = board.getValidMoves( turn );
        //     list<Move>::iterator it ;
        //     for ( it = moves.begin(); it != moves.end(); it++ )
        //     {
        //         OthelloBoard newBoard = board;
        //         newBoard.makeMove( turn, *it );
        //         MaxValue = max( MaxValue, minimax( newBoard, depth - 1, false ) );
        //     }
        //     return MaxValue;
        // }
        // else
        // {
        //     int MinValue = 20000;
        //     list<Move> moves = board.getValidMoves(turn);
        //     list<Move>::iterator it;
        //     for ( it = moves.begin(); it != moves.end(); it++ )
        //     {
        //         OthelloBoard newBoard = board;
        //         newBoard.makeMove( turn, *it );
        //         MinValue = min(MinValue, minimax( newBoard, depth - 1, true));
        //     }
        //     return MinValue;
        // }
    };

Move MyBot::play( const OthelloBoard& board )
{

    // board.print();
    // list<Move> moves = board.getValidMoves( turn );

    // int MaxValue = -20000;
    // Move& bestMove = moves.front();
    // list<Move>::iterator it;
    // for ( it = moves.begin(); it != moves.end(); it++ )
    // {
    //     OthelloBoard newBoard = board;
    //     newBoard.makeMove( turn, *it );
    //     int eval = minimax( newBoard, 4, false );
    //     if ( eval > MaxValue )
    //     {
    //         MaxValue = eval;
    //         bestMove = *it;
    //     }
    // }
    // return bestMove;
}

// The following lines are _very_ important to create a bot module for Desdemona

extern "C" {
    OthelloPlayer* createBot( Turn turn )
    {
        return new MyBot( turn );
    }

    void destroyBot( OthelloPlayer* bot )
    {
        delete bot;
    }
}
