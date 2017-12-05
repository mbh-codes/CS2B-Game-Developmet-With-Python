'''
import random
WORDS = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def get_random_word(wordDict):
    #This fuction returns a random string from the passed dictionary of lists of strings and its key
    #First, randomly select a key from its dictionary

    wordKey = random.choice(list(wordDict.keys()))
    #Second, randomly select a word from the key's list in the dictionary
    word_index = random.randint(0, len(wordDict[wordKey]) - 1)

    #print([wordDict[wordKey][word_index], wordKey]) #prints out a list
    return [wordDict[wordKey][word_index], wordKey]

secret_word, secret_set = get_random_word(WORDS)
print(secret_word)
print(secret_set)


counts = [1, 0, 0, 2, 2, 3, 8, 22, 33, 40, 45]
TOPSCORE = 10
#for s in range(TOPSCORE + 1):
#    print("{:2d}. {:3d} ({:5.2f}%)".format(s, counts[s], counts[s]/sum(counts)*100))

for s in range(TOPSCORE + 1):
    print(f"{s:2d}. {counts[s]:3d} ({counts[s]/sum(counts)*100:5.2f}%) {'*' * counts[s] }")

Expected Output
 0.   1 ( 0.64%)
 1.   0 ( 0.00%)
 2.   0 ( 0.00%)
 3.   2 ( 1.28%)
 4.   2 ( 1.28%)
 5.   3 ( 1.92%)
 6.   8 ( 5.13%)
 7.  22 (14.10%)
 8.  33 (21.15%)
 9.  40 (25.64%)
10.  45 (28.85%)


def remove_front_matter(linelist: [str]) -> [str]:
    # Return input list with starting lines (through "END OF FRONT MATTER") removed
    target_index = 0
    for test_index in range(len(linelist)):
        if 'END OF FRONT MATTER' == linelist[test_index]:
            target_index = test_index
    return linelist[target_index + 1:]

test_list = ["To be skipped",
             "Also to be skipped",
             "END OF FRONT MATTER",
             "To be included",
             "Also to be included"]
assert(remove_front_matter(test_list) == ["To be included",
                                          "Also to be included"])
assert(remove_front_matter(test_list[2:]) == ["To be included",
                                              "Also to be included"])
assert(remove_front_matter(test_list[:3]) == [ ])

def seconds_to_mmss(seconds: int) -> str:
    #Convert a number of seconds to minutes and seconds in "mm:ss" format
    rem_seconds =  seconds % 60
    minutes  = int(seconds/60)
    return str(minutes) + ":" + str(rem_seconds)
assert(seconds_to_mmss(15) == "0:15")
assert(seconds_to_mmss(75) == "1:15")
assert(seconds_to_mmss(3620) == "60:20")


find(...)
    S.find(sub) -> int
    Return the lowest index in S where the string sub is found.
    Return -1 on failure.
split(...)
    S.split(sep) -> list of strings
    Return a list of the words in S, using sep as the delimiter string.
strip(...)
    S.strip() -> str
#
60).zfill(2))
    Return a copy of the string S with leading and trailing whitespace removed.



MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
def mmddyy_to_MonthDayYear(mmddyy: str) -> str:
     #From an argument in the form '10/31/152' (month, day, year),
     #   return a string in the form 'October 31, 2015'.  Assume all
     #   values are valid numbers and all years are in this century
     #  (that means your function doesn't have to check).

    month_indicator = mmddyy.find('/')
    date_indicator = mmddyy[month_indicator+1:].find('/')
    month = MONTHS[int(mmddyy[0:month_indicator])-1]
    date = mmddyy[month_indicator+1: month_indicator + date_indicator + 1]
    year = mmddyy[month_indicator + date_indicator + 2 : ]
    return str(month) + ' '+ str(date) + ', 20' + str(year)

assert(mmddyy_to_MonthDayYear('10/31/15') == 'October 31, 2015')
assert(mmddyy_to_MonthDayYear('12/1/07') == 'December 1, 2007')
assert(mmddyy_to_MonthDayYear('1/3/99') == 'January 3, 2099')

'''


def zero_counts (top_value: int) -> 'list of int':
    ''' Return a list of zeroes, with one zero for each possible score from zero to
    top_value  '''
    result = []
    for i in range(top_value + 1):
        result.append(0)
    return result
assert zero_counts(10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert zero_counts(0) == [0]


quiz_scores = [18, 20, 18, 20, 0, 10, 10, 20, 10, 20]
quiz_counts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4]


def count_scores(scores: 'list of int', top_score: int) -> 'list of int':
    ''' Return a list that tallies the number of times each value (from 0
        to top_score) occurs in the list of scores
    '''
    mem_list = zero_counts(top_score)
    for i in scores:
        mem_list[i] += 1
    return mem_list



assert count_scores([], 5) == [0, 0, 0, 0, 0, 0]
assert count_scores(quiz_scores, 20) == quiz_counts

