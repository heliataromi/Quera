import unittest
from main import add_user, add_album, query_user_artist, query_user_genre, query_age_artist, query_age_genre, \
    query_city_artist, query_city_genre


class TestAll(unittest.TestCase):

    def setUp(self):
        self.judge_all_users = {}
        self.judge_all_albums = {}

        add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], self.judge_all_users, self.judge_all_albums)
        add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], self.judge_all_users, self.judge_all_albums)
        add_album("eclipse", "malmsteen", "classic", 10, self.judge_all_users)
        add_album("barf", "beeptunes", "pop", 22, self.judge_all_users)
        add_album("tekunbede", "beeptunes", "pop", 14, self.judge_all_users)
        add_album("gavazn", "sorena", "persian", 18, self.judge_all_users)

        add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], self.judge_all_users, self.judge_all_albums)
        add_album("bidad", "shajarian", "classic", 10, self.judge_all_users)
        add_album("blaze", "ghorbani", "pop", 9, self.judge_all_users)

    def test_query_user_artist_genre(self):
        self.assertEqual(query_user_artist("Ali", "ghorbani", self.judge_all_users, self.judge_all_albums), 9)
        self.assertEqual(query_user_genre("Ali", "classic", self.judge_all_users, self.judge_all_albums), 10)
        self.assertEqual(query_user_artist("SAliB", "sorena", self.judge_all_users, self.judge_all_albums), 18)
        self.assertEqual(query_user_artist("SAliB", "beeptunes", self.judge_all_users, self.judge_all_albums), 36)
        self.assertEqual(query_user_genre("SAliB", "pop", self.judge_all_users, self.judge_all_albums), 36)

    def test_query_age_artist_genre(self):
        self.assertEqual(query_age_artist(22, "malmsteen", self.judge_all_users, self.judge_all_albums), 10)
        self.assertEqual(query_age_genre(19, "pop", self.judge_all_users, self.judge_all_albums), 36)
        self.assertEqual(query_age_artist(12, "shajarian", self.judge_all_users, self.judge_all_albums), 10)
        self.assertEqual(query_age_genre(12, "pop", self.judge_all_users, self.judge_all_albums), 9)

    def test_query_city_artist_genre(self):
        self.assertEqual(query_city_artist("Bushehr", "ghorbani", self.judge_all_users, self.judge_all_albums), 9)
        self.assertEqual(query_city_genre("Bushehr", "pop", self.judge_all_users, self.judge_all_albums), 9)
        self.assertEqual(query_city_artist("Tehran", "sorena", self.judge_all_users, self.judge_all_albums), 18)
        self.assertEqual(query_city_genre("Tehran", "pop", self.judge_all_users, self.judge_all_albums), 36)
