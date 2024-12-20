from variables import *
from chart_patterns import *

class Chart_HHM():
    def __init__(self):
        self.song_name = 'Hmm Heu Ming Remix (Rcol)' 

    def build_chart(self,full_path):
        global wait_delay

        song_length = 104200
        song_bpm = 112
        song_mpb = ((1000 * 60 / song_bpm)) 
        song_difficulty = 4
        number_of_nodes = 199
        recommended_fps = 120

        song_offset = 10650

        if self.song_name == 'HHM_climax':
            song_offset = -520
        s1 = 426
        s2 = s1//2
        s3 = s2 + s1//4
        s4 = s1//4
        s8 = s1//8  # 53
        s16 = s1//16  # 26
        s32 = s1//32
        ming = s8*6

        if self.song_name == 'HHM_C':
            song_offset = -380
        t1 = s1 - s8 - s16 + 10 # 356
        t2 = t1//2 # 178
        t4 = t1//4 # 89
        t8 = t1//8 # 44
        t16 = t1//16 # 22
        t32 = t1//32  # 11
        tex = t1+1

        if self.song_name == 'HHM_D':
            song_offset = 60
        d1 = s1 - s8 - s16 + 6

        if self.song_name == 'HHM_E':
            song_offset = -30
        e1 = t1 - t4   # 267
        e3 = e1 + e1//2

        ee = 5 * e1 + t8 + 40 # 1420
        ee4 = ee//4  # 355
        egap = 25

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            beat_pos = song_offset
            for j in range(2):
                for i in range(2):
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s16  # s8
                    f.write(pattern)

                    ### 흠 흐 흠
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)
                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    if i == 0:  
                        beat_pos += s8 + s16
                        pattern = basic_hold(beat_pos, 3, 1, s1 - s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        beat_pos += s4 + s16 + s32
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)

            for k in range(2):
                for j in range(2):
                    for i in range(3):
                        pattern = basic_hold(beat_pos, 1, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 3, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                    if j == 0:
                        pattern = basic_hold(beat_pos, 3, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 1, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                    elif j == 1 and k == 0:
                        pattern = basic_hold(beat_pos, 3, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                        beat_pos += t8 - s16
                        pattern = basic_strike(beat_pos, 4, 1)
                        beat_pos += t1 - t8
                        f.write(pattern)

                        beat_pos += t32  
                    else:  
                        beat_pos += s16
                        for kk in range(2):
                            pattern = basic_strike(beat_pos, 1, 1)
                            beat_pos += t2 + 22
                            f.write(pattern)

                            pattern = basic_strike(beat_pos, 3, 1)
                            beat_pos += t2
                            f.write(pattern)

            beat_pos -= t16  

            pattern = basic_hold(beat_pos, 1, 1, t1)
            beat_pos += t1
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2 - t8 - t16
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t2 + t4 + t32
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += t2 - t32
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t2
            f.write(pattern)

            beat_pos += t2 + t4 - t8  # correction

            pattern = basic_hold(beat_pos, 1, 1, t1 - t4)
            beat_pos += t1 - t8
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2 - t16
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t2 + t4
            f.write(pattern)

            pattern = basic_hold(beat_pos, 1, 1, t1 - t4)
            beat_pos += t1 - t8
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2 - t16
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t1 + t2 + t16
            f.write(pattern)

            ######### Type D-2:
            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 2 * t1
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 2 * t1
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 2 * t1
            f.write(pattern)

            pattern = basic_strike(beat_pos - t16, 4, 1)
            beat_pos += t1
            f.write(pattern)

            for j in range(2):
                for i in range(3):
                    pattern = basic_hold(beat_pos, 1, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 3, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                if j == 0:
                    pattern = basic_hold(beat_pos, 3, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 1, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                else:
                    pattern = basic_hold(beat_pos, 3, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 4, 1, t4)
                    beat_pos += tex
                    f.write(pattern)

            beat_pos -= t16 

            for j in range(2):
                for i in range(2):
                    pattern = basic_hold(beat_pos, 1, 1, t2)
                    beat_pos += t1 - t8
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += e1
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += 3 * e1
                    f.write(pattern)

                pattern = basic_strike(beat_pos, 3, 1)
                beat_pos += e3
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += 3 * e1 + e3 // 2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += e3
                f.write(pattern)

                pattern = basic_strike(beat_pos, 3, 1)
                beat_pos += 4 * e1 + e1 // 4
                f.write(pattern)

            beat_pos -= e1 // 2 #- 100

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee
            f.write(pattern)

            beat_pos += ee4

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4 * 2
            f.write(pattern)

            # drum beats
            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4 * 2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4 * 2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee + ee // 2  # - ee4//2
            f.write(pattern)

            pattern = basic_hold(beat_pos, 4, 1, ee - 100)
            beat_pos += ee - ee4 // 2
            f.write(pattern)

            beat_pos += ee // 4 

            for j in range(2):
                for i in range(2):

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s16  # s8
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    if i == 0:  
                        beat_pos += s8 + s16
                        pattern = basic_hold(beat_pos, 3, 1, s1 - s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        beat_pos += s4 + s16 + s32
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)

            beat_pos += 0  

            for j in range(2):
                for i in range(2):
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s16  
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    if i == 0:  
                        beat_pos += s8 + s16
                        pattern = basic_hold(beat_pos, 3, 1, s1 - s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        beat_pos += s4 + s16 + s32
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)

            beat_pos += 0  





