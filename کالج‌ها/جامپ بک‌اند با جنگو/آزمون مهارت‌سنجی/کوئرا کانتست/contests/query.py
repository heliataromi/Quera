from django.contrib.auth import get_user_model
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.db.models import F, Q, Sum

from problems.models import Submission, Problem
from .models import Contest
User = get_user_model()


def list_problems(contest_id):
    query = Contest.objects.get(id=contest_id).problems.get_queryset()
    return query


def list_users(contest_id):
    query = Contest.objects.get(id=contest_id).participants.get_queryset()
    return query


def list_submissions(contest_id):
    query = Submission.objects.filter(problem__in=list_problems(contest_id)).order_by('-submitted_time')
    return query


def list_problem_submissions(contest_id, problem_id):
    query = list_submissions(contest_id).filter(problem=problem_id)
    return query


def list_user_submissions(contest_id, user_id):
    query = list_submissions(contest_id).filter(participant=user_id)
    return query


def list_problem_user_submissions(contest_id, user_id, problem_id):
    query = list_problem_submissions(contest_id, problem_id).filter(participant=user_id)
    return query


def list_users_solved_problem(contest_id, problem_id):
    query = list_problem_submissions(contest_id, problem_id).filter(score__exact=F('problem__score')).values_list('participant', flat=True)
    q = User.objects.filter(id__in=query)
    return q


def user_score(contest_id, user_id):
    scores = dict()
    for submission in list_user_submissions(contest_id, user_id):
        if submission.problem not in scores.keys():
            scores[submission.problem] = [submission.score]
        else:
            scores[submission.problem].append(submission.score)
    return sum([max(problem) for problem in scores.values()])


def list_final_submissions(contest_id):
    query = list_submissions(contest_id).filter(score__gte=max(list_submissions(contest_id).filter(Q(problem=F('problem')) & Q(participant=F('participant'))).values_list('score', flat=True)))
    return query.values('participant_id', 'problem_id', 'score')
