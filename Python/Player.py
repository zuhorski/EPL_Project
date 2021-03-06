import pandas as pd
from PL_Standings import xStandings, fix
import numpy as np

# This is STEP 3 of the process to create the new season file
s = xStandings()


class Player:
    def __init__(self, teams, player_name=None):
        self.players_teams = teams
        self.player_name = player_name

    def teams_fixture_results(self):
        return fix.fixture_list_df[(fix.fixture_list_df["Home"].isin(self.players_teams)) | (
            fix.fixture_list_df["Away"].isin(self.players_teams))].reset_index(drop=True)

    def mini_standings(self):
        players_teams_mini_standings = s.standings[s.standings["Team"].isin(self.players_teams)].reset_index(drop=True)
        return players_teams_mini_standings

    def expected_mini_standings(self):
        players_teams_exp_mini_standings = s.xStandings[s.xStandings["Team"].isin(self.players_teams)].reset_index(drop=True)
        return players_teams_exp_mini_standings

    def summary_statistics(self):
        sum_stats = self.mini_standings().agg([sum, np.mean, max, min]).transpose().drop("Team")
        sum_stats_df = pd.DataFrame(sum_stats)
        return sum_stats_df

    def expected_summary_stats(self):
        xsum_stats = self.expected_mini_standings().agg([sum, np.mean, max, min]).transpose().drop("Team")
        xsum_stats_df = pd.DataFrame(xsum_stats)
        return xsum_stats_df

    def cumulative_weekly_points(self, weeks=None):
        weeks = weeks
        total_teams_weekly_pts = []
        if weeks == None:
            min_games = self.summary_statistics()["min"]["MP"]
        else:
            min_games = weeks
        points = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Winner"][row] == i:
                    points += 3
                elif team["Winner"][row] == "Tie":
                    points += 1
            total_teams_weekly_pts.append(points)
        return total_teams_weekly_pts

    def cumulative_Xweekly_points(self, weeks=None):
        weeks = weeks
        total_teams_weekly_pts = []
        if weeks == None:
            min_games = self.expected_summary_stats()["min"]["MP"]
        else:
            min_games = weeks
        points = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["xWinner"][row] == i:
                    points += 3
                elif team["xWinner"][row] == "Tie":
                    points += 1
            total_teams_weekly_pts.append(points)
        return total_teams_weekly_pts

    def cumulative_weekly_wins(self, weeks=None):
        weeks = weeks
        total_teams_weekly_wins = []
        if weeks == None:
            min_games = self.summary_statistics()["min"]["MP"]
        else:
            min_games = weeks
        wins = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Winner"][row] == i:
                    wins += 1
            total_teams_weekly_wins.append(wins)
        return total_teams_weekly_wins

    def cumulative_Xweekly_wins(self, weeks=None):
        weeks = weeks
        total_teams_weekly_wins = []
        if weeks == None:
            min_games = self.expected_summary_stats()["min"]["MP"]
        else:
            min_games = weeks
        wins = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["xWinner"][row] == i:
                    wins += 1
            total_teams_weekly_wins.append(wins)
        return total_teams_weekly_wins

    def cumulative_weekly_losses(self, weeks=None):
        weeks = weeks
        total_teams_weekly_losses = []
        if weeks == None:
            min_games = self.summary_statistics()["min"]["MP"]
        else:
            min_games = weeks
        losses = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Loser"][row] == i:
                    losses += 1
            total_teams_weekly_losses.append(losses)
        return total_teams_weekly_losses

    def cumulative_Xweekly_loss(self, weeks=None):
        weeks = weeks
        total_teams_weekly_losses = []
        if weeks == None:
            min_games = self.expected_summary_stats()["min"]["MP"]
        else:
            min_games = weeks
        losses = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["xLoser"][row] == i:
                    losses += 1
            total_teams_weekly_losses.append(losses)
        return total_teams_weekly_losses

    def cumulative_weekly_ties(self, weeks= None):
        weeks = weeks
        total_teams_weekly_ties = []
        if weeks == None:
            min_games = self.summary_statistics()["min"]["MP"]
        else:
            min_games = weeks
        ties = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Loser"][row] == "Tie":
                    ties += 1
            total_teams_weekly_ties.append(ties)
        return total_teams_weekly_ties

    def cumulative_Xweekly_ties(self, weeks=None):
        weeks = weeks
        total_teams_weekly_ties = []
        if weeks == None:
            min_games = self.expected_summary_stats()["min"]["MP"]
        else:
            min_games = weeks
        ties = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["xLoser"][row] == "Tie":
                    ties += 1
            total_teams_weekly_ties.append(ties)
        return total_teams_weekly_ties

    def cumulative_weekly_goals_for(self, weeks=None):
        weeks = weeks
        total_teams_weekly_GF = []
        if weeks == None:
            min_games = self.summary_statistics()["min"]["MP"]
        else:
            min_games = weeks
        GF = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Home"][row] == i:
                    g = team["Score"][row]
                    GF += int(g[0])
                elif team["Away"][row] == i:
                    g = team["Score"][row]
                    GF += int(g[2])
            total_teams_weekly_GF.append(GF)
        return total_teams_weekly_GF

    def cumulative_Xweekly_goals_for(self, weeks=None):
        weeks = weeks
        total_teams_weekly_GF = []
        if weeks == None:
            min_games = self.expected_summary_stats()["min"]["MP"]
        else:
            min_games = weeks
        GF = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Home"][row] == i:
                    g = team["xG"][row]
                    GF += int(g)
                elif team["Away"][row] == i:
                    g = team["xG.1"][row]
                    GF += int(g)
            total_teams_weekly_GF.append(GF)
        return total_teams_weekly_GF

    # def _weekly_goals_for(self):
    #     i = 0
    #     weekly_gf = []
    #     for i in range(len(self.cumulative_weekly_goals_for())):
    #         if i == 0:
    #             weekly_gf.append(self.cumulative_weekly_goals_for()[i])
    #         else:
    #             gf = int(self.cumulative_weekly_goals_for()[i]) - int(self.cumulative_weekly_goals_for()[i-1])
    #             weekly_gf.append(gf)
    #     return weekly_gf

    def cumulative_weekly_goals_against(self, weeks=None):
        weeks = weeks
        total_teams_weekly_GA = []
        if weeks == None:
            min_games = self.summary_statistics()["min"]["MP"]
        else:
            min_games = weeks
        GA = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Home"][row] == i:
                    g = team["Score"][row]
                    GA += int(g[2])
                elif team["Away"][row] == i:
                    g = team["Score"][row]
                    GA += int(g[0])
            total_teams_weekly_GA.append(GA)
        return total_teams_weekly_GA

    def cumulative_Xweekly_goals_against(self, weeks=None):
        weeks = weeks
        total_teams_weekly_GA = []
        if weeks == None:
            min_games = self.expected_summary_stats()["min"]["MP"]
        else:
            min_games = weeks
        GA = 0
        for row in range(int(min_games)):
            for i in self.players_teams:
                team = (fix.fixture_list_df[
                    (fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")]).reset_index(
                    drop=True)
                if team["Home"][row] == i:
                    g = team["xG.1"][row]
                    GA += int(g)
                elif team["Away"][row] == i:
                    g = team["xG"][row]
                    GA += int(g)
            total_teams_weekly_GA.append(GA)
        return total_teams_weekly_GA

    # def _weekly_goals_against(self):
    #     i =0
    #     weekly_ga = []
    #     for i in range(len(self.cumulative_weekly_goals_against())):
    #         if i == 0:
    #             weekly_ga.append(self.cumulative_weekly_goals_against()[i])
    #         else:
    #             ga = int(self.cumulative_weekly_goals_against()[i]) - int(self.cumulative_weekly_goals_against()[i-1])
    #             weekly_ga.append(ga)
    #     return weekly_ga

    def weekly_df(self, weeks=None):
        # Gives the option of choosing up to what week you want
        weeks = weeks
        mp = []
        if weeks == None:
            for i in range(1, int(self.summary_statistics()["min"]["MP"]) + 1):
                mp.append(i)
        else:
            for i in range(1, weeks + 1):
                mp.append(i)

        weekly_df = pd.DataFrame()
        weekly_df["Mp"] = mp
        weekly_df["Wins"] = self.cumulative_weekly_wins(mp[-1])
        weekly_df["Ties"] = self.cumulative_weekly_ties(mp[-1])
        weekly_df["Loss"] = self.cumulative_weekly_losses(mp[-1])
        weekly_df["Points"] = self.cumulative_weekly_points(mp[-1])
        weekly_df["Tot_GF"] = self.cumulative_weekly_goals_for(mp[-1])
        #weekly_df["Wk_GF"] = self._weekly_goals_for()
        weekly_df["Tot_GA"] = self.cumulative_weekly_goals_against(mp[-1])
        #weekly_df["Wk_GA"] = self._weekly_goals_against()
        weekly_df["GD"] = weekly_df["Tot_GF"] - weekly_df["Tot_GA"]
        #weekly_df = weekly_df.set_index("Mp")
        return weekly_df

    def xWeekly_df(self, weeks=None):
        # Gives the option of choosing up to what week you want
        weeks = weeks
        mp = []
        if weeks == None:
            for i in range(1, int(self.expected_summary_stats()["min"]["MP"]) + 1):
                mp.append(i)
        else:
            for i in range(1, weeks + 1):
                mp.append(i)

        xweekly_df = pd.DataFrame()
        xweekly_df["Mp"] = mp
        xweekly_df["xWins"] = self.cumulative_Xweekly_wins(mp[-1])
        xweekly_df["xTies"] = self.cumulative_Xweekly_ties(mp[-1])
        xweekly_df["xLoss"] = self.cumulative_Xweekly_loss(mp[-1])
        xweekly_df["xPts"] = self.cumulative_Xweekly_points(mp[-1])
        xweekly_df["xTot_GF"] = self.cumulative_Xweekly_goals_for(mp[-1])
        #weekly_df["Wk_GF"] = self._weekly_goals_for()
        xweekly_df["xTot_GA"] = self.cumulative_Xweekly_goals_against(mp[-1])
        #weekly_df["Wk_GA"] = self._weekly_goals_against()
        xweekly_df["xGD"] = xweekly_df["xTot_GF"] - xweekly_df["xTot_GA"]
        #weekly_df = weekly_df.set_index("Mp")
        return xweekly_df


bran = Player(["Liverpool","Arsenal","Everton","Aston Villa","Wolves"], "Brandon")
eli = Player(["Manchester City","Tottenham","Brighton","Watford","Norwich City"], "Eli")
mal = Player(["Manchester Utd","West Ham","Southampton","Burnley","Brentford"], "Malachi")
sab = Player(["Chelsea","Leicester City","Leeds United","Newcastle Utd","Crystal Palace"], "Sabastian")




