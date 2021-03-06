
# two string constants
ARROW = '-> '
NULL = ''
ZERO = 0
ONE = 1

#
# the color light-blue
#
lightblue = (43,169,255)


#
# a couple of rotation, translation, scaling vectors
#
rts1 = [[3.0,3.1,2.0],[2.2, 1.2, 2.0], [0.8,0.8,0.8]]
rts2 = [[3.2,2.6,1.8],[-1.9, 1.2, 1.6], [0.3,0.3,1.0]]
rts3 = [[2.2,3.3,1.4], [-1.0, 1.2,-1.5], [0.6,0.6, 0.6]]
rts4 = [[4.2,2.1,3.2],[1.2, 1.3, 1.0],[0.5,0.5,0.8]]
rts5 = [[1.2,3.3,2.4], [-2.0, 1.4,-2.1], [0.8, 0.8, 0.2]]
rts6 = [[3.2,3.6,2.4], [1.1, 1.6, 2.5], [0.8,0.3,0.1]]
rts7 = [[2.3,2.7,3.3], [1.1, 2.3, 1.7], [0.6,0.6,0.5]]
rts8 = [[4.2,2.1,3.2], [1.2, 1.3, 0.0], [0.5,0.5,0.5]]
#
rts90 = [[4.2,2.1,3.2], [2.0, 0.0, 0.9], [0.3,0.3,1.0]]
rts91 = [[4.2,2.1,3.2], [-2.0, 0.0, 0.9], [0.3,0.3,1.0]]
rts92 = [[4.2,2.1,3.2], [0.0, 2.0, 0.9], [0.3,0.3,1.0]]
rts93 = [[4.2,2.1,3.2], [0.0, -2.0, 0.9], [0.3,0.3,1.0]]
rts10 = [[4.2,2.1,3.2], [0.0, 0.0, 0.0], [2.2,2.2,0.2]]

#
# (composite) object definitions
#
o1 = [['sphere',rts1, 1]]
o2 = [['cylinder', rts2, 4]]
o3 = [['cube', rts3, 3]]
o4 = [['cone', rts4, 2], ['sphere', rts8, 9]]
o5 = [['sphere', rts5, 5]]
o6 = [['cube', rts6, 6]]
o7 = [['pyramid', rts7, 8]]
o8 = [['cube', rts10, 9], ['cylinder', rts90, 2], ['cylinder', rts91, 2], ['cylinder', rts92, 2], ['cylinder', rts93, 2]]
