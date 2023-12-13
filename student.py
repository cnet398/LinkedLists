class Students:
    def __init__(self, last_name, first_name, ssn, email, age):
      self.mLastname = last_name
      self.mFirstname = first_name
      self.mSsn = ssn
      self.mEmail = email
      self.mAge = age
    def __eq__(self,rhs):
        if self.mSsn == rhs: #or rhs.mSsn
            return True
        else:
            return False