#!/usr/bin/env python3
"""
Rap Battle - A fun command-line rap battle game
"""
import random
import time
from typing import List, Dict

class Rapper:
    """Represents a rapper with unique style and rhymes"""
    
    def __init__(self, name: str, style: str, rhymes: List[str]):
        self.name = name
        self.style = style
        self.rhymes = rhymes
        self.score = 0
    
    def drop_verse(self) -> str:
        """Return a random verse from the rapper's collection"""
        return random.choice(self.rhymes)
    
    def __str__(self):
        return f"{self.name} ({self.style})"


class RapBattle:
    """Manages the rap battle between two rappers"""
    
    def __init__(self, rapper1: Rapper, rapper2: Rapper, rounds: int = 3):
        self.rapper1 = rapper1
        self.rapper2 = rapper2
        self.rounds = rounds
        self.current_round = 0
    
    def judge_round(self, verse1: str, verse2: str) -> int:
        """
        Judge a round based on verse complexity and length
        Returns 1 if rapper1 wins, 2 if rapper2 wins, 0 for tie
        """
        score1 = len(verse1) + random.randint(1, 10)
        score2 = len(verse2) + random.randint(1, 10)
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0
    
    def print_separator(self):
        """Print a visual separator"""
        print("\n" + "=" * 60 + "\n")
    
    def battle(self):
        """Run the rap battle"""
        print(f"\n🎤 RAP BATTLE: {self.rapper1.name} vs {self.rapper2.name} 🎤")
        print(f"Style: {self.rapper1.style} vs {self.rapper2.style}")
        self.print_separator()
        
        for round_num in range(1, self.rounds + 1):
            self.current_round = round_num
            print(f"🔥 ROUND {round_num} 🔥\n")
            
            # Rapper 1's turn
            print(f"🎵 {self.rapper1.name} steps up:")
            time.sleep(1)
            verse1 = self.rapper1.drop_verse()
            print(f'"{verse1}"')
            time.sleep(1.5)
            
            self.print_separator()
            
            # Rapper 2's turn
            print(f"🎵 {self.rapper2.name} responds:")
            time.sleep(1)
            verse2 = self.rapper2.drop_verse()
            print(f'"{verse2}"')
            time.sleep(1.5)
            
            self.print_separator()
            
            # Judge the round
            winner = self.judge_round(verse1, verse2)
            if winner == 1:
                self.rapper1.score += 1
                print(f"🏆 {self.rapper1.name} wins this round!")
            elif winner == 2:
                self.rapper2.score += 1
                print(f"🏆 {self.rapper2.name} wins this round!")
            else:
                print("🤝 It's a tie!")
            
            print(f"\nScore: {self.rapper1.name} {self.rapper1.score} - {self.rapper2.score} {self.rapper2.name}")
            self.print_separator()
            time.sleep(1)
        
        # Announce winner
        self.announce_winner()
    
    def announce_winner(self):
        """Announce the final winner"""
        print("\n" + "🎊" * 30)
        print("\n🏁 FINAL RESULTS 🏁\n")
        print(f"{self.rapper1.name}: {self.rapper1.score} points")
        print(f"{self.rapper2.name}: {self.rapper2.score} points\n")
        
        if self.rapper1.score > self.rapper2.score:
            print(f"🎉 WINNER: {self.rapper1.name}! 🎉")
        elif self.rapper2.score > self.rapper1.score:
            print(f"🎉 WINNER: {self.rapper2.name}! 🎉")
        else:
            print("🤝 IT'S A TIE! Both rappers killed it! 🤝")
        
        print("\n" + "🎊" * 30 + "\n")


def create_default_rappers() -> List[Rapper]:
    """Create a list of default rappers with pre-written verses"""
    
    mc_flow = Rapper(
        name="MC Flow",
        style="Smooth Flow",
        rhymes=[
            "I'm the lyrical miracle, spitting vernacular, my flow so spectacular",
            "Rhythm in my veins, poetry in my brain, I bring the heat like a flame",
            "Words like weapons, bars like blessing, teaching you a lesson",
            "I'm the architect of rhyme, building verses all the time",
            "Microphone controller, hip-hop soldier, getting bolder as I get older"
        ]
    )
    
    rhythm_king = Rapper(
        name="Rhythm King",
        style="Hard Hitting",
        rhymes=[
            "I'm the king on this throne, ruling the zone, with a style all my own",
            "Beats drop heavy, I stay ready, flow so steady like confetti",
            "Crushing competition with my lyrical ammunition and precision",
            "Born to reign, can't contain, the power in my brain",
            "I'm the definition of ambition, on a lyrical mission"
        ]
    )
    
    lyric_ace = Rapper(
        name="Lyric Ace",
        style="Wordplay Master",
        rhymes=[
            "I flip words like acrobatics, my style's automatic, so dramatic",
            "Metaphors and similes, creating lyrical symphonies with ease",
            "I'm painting pictures with my diction, pure linguistic fiction",
            "Rhyme schemes so complex, leaving rappers perplexed",
            "Vocabulary vast, I'm rapping fast, built to last"
        ]
    )
    
    beat_boxer = Rapper(
        name="Beat Boxer",
        style="Rhythmic Genius",
        rhymes=[
            "Boom bap boom, I light up the room, sealing your doom",
            "Percussion in my mouth, going south to north, bringing forth the force",
            "I'm the human drum machine, keeping it clean, know what I mean",
            "Beatboxing and rapping, multitasking, no asking, I'm everlasting",
            "Rhythm is my language, speaker of savage, lyrical advantage"
        ]
    )
    
    return [mc_flow, rhythm_king, lyric_ace, beat_boxer]


def main():
    """Main function to run the rap battle"""
    print("\n" + "🎤" * 30)
    print(" " * 20 + "RAP BATTLE ARENA")
    print("🎤" * 30 + "\n")
    
    rappers = create_default_rappers()
    
    print("Available Rappers:")
    for i, rapper in enumerate(rappers, 1):
        print(f"{i}. {rapper}")
    
    print("\nStarting a random battle...\n")
    time.sleep(1)
    
    # Select two random rappers
    battlers = random.sample(rappers, 2)
    
    # Create and run the battle
    battle = RapBattle(battlers[0], battlers[1], rounds=3)
    battle.battle()


if __name__ == "__main__":
    main()
