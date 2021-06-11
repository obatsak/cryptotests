import time


class App ():

    def __init__ (self, kList, roundNum, samples):
        self.kList = kList
        self.roundNum = roundNum
        self.samples = samples
        

    def hashTest(self, hashFunc):
        for k in self.kList:
            result = []
            for n in range(0, self.samples):
                try:
                    data = ' '.encode() * 1024 * 1024 * k
                except BaseException as Err:
                    print('On {0}MB take error: {1}'.format(k, Err))
                else:
                    t1 = time.time()
                    hashFunc(data)
                    t2 = time.time() - t1
                    result.append(t2)
            if len(result) > 0:
                print('For hash algoritm {} and size {}MB result: min {}sec, max {}sec, avg {}sec.'.format(hashFunc.__name__, k, round(min(result), self.roundNum), round(max(result), 
                                                                                                self.roundNum), round(sum(result)/len(result), self.roundNum) ))
            else:
                print('For hash algoritm {} and {}MB size has no successful results.'.format(hashFunc.__name__, k) )
            


