from random import randrange
from pythonds.basic.queue import Queue

class patient:
    def __init__(self, time):
        self.time_stamp = time
        self.age = randrange(20, 61)
    def getstamp(self):
        return self.time_stamp
    def get_age(self):
        return self.age
    def wait_time(self, current_time):
        return current_time - self.time_stamp

class doctor:
    def __init__(self, patient_Rate):
        self.patientRate = patient_Rate
        self.current_patient = None
        self.timeRemaining = 0

    def tick(self):
        if self.current_patient != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining == 0:
                self.current_patient = None

    def busy(self):
        if self.current_patient != None:  # return self.current_patient != None
            return True
        else:
            return False

    def next_patient(self, new_patient):
        self.current_patient = new_patient
        self.timeRemaining = round((new_patient.get_age() / self.patientRate)*60)

def simulation(num_seconds, patient_per_minute):
    clinic_doctor = doctor(patient_per_minute)
    patient_queue = Queue()
    waitingtime = []
    for current_second in range(num_seconds):
         if randrange(1, 361) == 360:
             Patient = patient(current_second)
             patient_queue.enqueue(Patient)

         if (not clinic_doctor.busy()) and (not patient_queue.isEmpty()):
             new_Patient = patient_queue.dequeue()
             waitingtime.append(new_Patient.wait_time(current_second))
             clinic_doctor.next_patient(new_Patient)
         clinic_doctor.tick()

    average_wait = (sum(waitingtime) / len(waitingtime)) / 60
    print("average wait : ", "{:.2f}".format(average_wait), "(minutes)", '  &   ',patient_queue.size(), "patient remining.")
    
for i in range(10):
    simulation(14400, 10)

