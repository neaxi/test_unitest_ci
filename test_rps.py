#!/usr/bin/python3

import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_play():
    assert rps.is_valid_play("rock")
    
def test_paper_is_valid_play():
    assert rps.is_valid_play("paper")

def test_scissors_is_valid_play():
    assert rps.is_valid_play("scissors")

def test_lizard_is_invalid_play():
    assert rps.is_valid_play("lizard") is False




def test_computer_play_is_valid():
    for _ in range(2000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    repeats = 2000
    prcntage = 0.3
    plays = [rps.generate_computer_play() for _ in range(repeats)]
    
    # prints only if assert fails
    print([i + ": " + str(plays.count(i)) for i in ['rock', 'paper', 'scissors']])
    
    assert plays.count('rock') > repeats * prcntage
    assert plays.count('paper') > repeats * prcntage
    assert plays.count('scissors') > repeats * prcntage

    
def test_rock_beats_rock():
    result = rps.eval_game('rock', 'rock')
    assert result == 'tie'
    
def test_rock_beats_paper():
    result = rps.eval_game('rock', 'paper')
    assert result == 'computer'
    
def test_rock_beats_scissors():
    result = rps.eval_game('rock', 'scissors')
    assert result == 'human'

def test_paper_beats_rock():
    result = rps.eval_game('paper', 'rock')
    assert result == 'human' 
    
def test_paper_beats_paper():
    result = rps.eval_game('paper', 'paper')
    assert result == 'tie'
    
def test_paper_beats_scissors():
    result = rps.eval_game('paper', 'scissors')
    assert result == 'computer'
    
def test_scissors_beats_rock():
    result = rps.eval_game('scissors', 'rock')
    assert result == 'computer'
    
def test_scissors_beats_paper():
    result = rps.eval_game('scissors', 'paper')
    assert result == 'human'
    
def test_scissors_beats_scissors():
    result = rps.eval_game('scissors', 'scissors')
    assert result == 'tie'


def input_faked_rock(prompt):
    print(prompt)
    return 'scissors'

@pytest.fixture
def fake_input_rock(monkeypatch):
    monkeypatch.setattr('builtins.input', input_faked_rock)
    


def test_full_game(capsys, fake_input_rock):
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert 'rock, paper or scissors? ' in captured.out




def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run(['python', 'rps.py'], 
                        encoding='utf-8',
                        stdout=subprocess.PIPE,
                        input='dragon\nrock\n', 
                        check=True)
    assert cp.stdout.count('rock, paper or scissors? ') == 2
