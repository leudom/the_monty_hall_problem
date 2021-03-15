#!/usr/bin/env python
# Import random module
import random
import argparse
import time

if __name__ == '__main__':

    # Now we parse our args into the script
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials', type=int, default=100000, help='Number of trials you wanna play (default=100000)')
    args = parser.parse_args()

    # Init dict to count for winning a game when either stayed or switched the doors
    results = {'won_when_stayed': 0, 'won_when_switched': 0}
    doors = set(range(1, 4))

    print('Start playing %i times...' % (args.trials))
    start_time = time.time()

    # For each game do the following...
    for i in range(args.trials):

        # Sample one door to be the players initialy chosen door
        door_player = random.sample(doors,1).pop()
        # Sample one door to be the door with the prize behind
        door_prize = random.sample(doors,1).pop()

        # Now first get the door that the showmaster will open...
        door_opened = random.sample(doors.difference(set((door_player, door_prize))),1).pop()
        # ...and then the one that remains --> This is the alternative to switch to!
        door_to_switch = random.sample(doors.difference(set((door_opened, door_player))),1).pop()
        
        # Now get the two scenarios and count for the winning situations in the results dict
        # Case 1: Player stays on initialy chosen door
        if door_prize == door_player:
            results['won_when_stayed'] += 1
        # Case 2: Player switches to the alternative door
        if door_prize == door_to_switch:
            results['won_when_switched'] += 1

    timed = time.time() - start_time
    print('Finished all trials in %f seconds' % timed)

    print('Absolute number of winning a game when stayed: %i' % results['won_when_stayed'])
    print('Absolute number of winning a game when switched to the alternative door: %i' % results['won_when_switched'])
    rel_freq_switched = results['won_when_switched'] / (results['won_when_switched'] + results['won_when_stayed'])
    print('Relative frequency of winning the prize when switching the doors: %0.4f' % rel_freq_switched)