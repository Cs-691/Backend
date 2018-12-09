
class Algorithm():
   
    dt=None
    cols=None
   
    def __init__(self):
       


        import pandas as pd
        
        
        # In[2]:
        
        
        import csv
        from collections import defaultdict
        
        
        # In[3]:
        
        
        columns = ['Source','Target','Weight']
        
        
        # In[4]:
        
        
        data = pd.read_csv("Scraped-Data/dataset_clean.csv")
        
        
        # In[5]:
        
        
        df = pd.DataFrame(data)
        
        
        # In[6]:
        
        
        df_s = df['Source']
        
        
        # In[7]:
        
        
        df_1 = pd.get_dummies(df.Target)
        
        
        # In[8]:
        
        
        df_pivoted = pd.concat([df_s,df_1], axis=1)
        
        
        # In[9]:
        
        
        self.cols = df_pivoted.columns
        
        
        
        self.cols = self.cols[1:]
        
        
        # In[11]:
        
        
        x = df_pivoted[self.cols]
        y = df_pivoted['Source']
        
        
        # ### Trying out our classifier to learn diseases from the symptoms
        
        # In[12]:
        
        
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.cross_validation import train_test_split
        
        
        # In[13]:
        
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        
        
        # In[14]:
        
        
        mnb = MultinomialNB()
        mnb = mnb.fit(x_train, y_train)
        
        
        # In[15]:
        
        
        mnb_tot = MultinomialNB()
        mnb_tot = mnb_tot.fit(x, y)
        
        
        # In[16]:
        
        
        disease_pred = mnb_tot.predict(x)
        
        
        # In[17]:
        
        
        disease_real = y.values
        
        
        # ### Training a decision tree
        
        # In[18]:
        
        
        from sklearn.tree import DecisionTreeClassifier
        
        
        # In[19]:
        
        
        self.dt = DecisionTreeClassifier()
        clf_dt=self.dt.fit(x,y)
        
        
        # In[20]:
        
        
        from sklearn import tree 
        
        
        # ## Analysis of the Manual data
        
        # In[21]:
        
        
        data = pd.read_csv("Manual-Data/Training.csv")
        
        
        # In[22]:
        
        
        df = pd.DataFrame(data)
        
        
        # In[23]:
        
        
        self.cols = df.columns
        
        
        # In[24]:
        
        
        self.cols = self.cols[:-1]
        
        
        # In[25]:
        
        
        x = df[self.cols]
        y = df['prognosis']
        
        
        # ### Trying out our classifier to learn diseases from the symptoms
        
        # In[26]:
        
        
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.cross_validation import train_test_split
        
        
        # In[27]:
        
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        
        
        # In[28]:
        
        
        mnb = MultinomialNB()
        mnb = mnb.fit(x_train, y_train)
        
        
        # In[29]:
        
        
        from sklearn import cross_validation
        scores = cross_validation.cross_val_score(mnb, x_test, y_test, cv=3)
        
        
        # In[30]:
        
        
        test_data = pd.read_csv("Manual-Data/Testing.csv")
        
        
        # In[31]:
        
        
        testx = test_data[self.cols]
        testy = test_data['prognosis']
        
        
        # ### Training a decision tree
        
        # In[32]:
        
        
        from sklearn.tree import DecisionTreeClassifier
        
        
        # In[33]:
        
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        
        
        # In[34]:
        
        
        self.dt = DecisionTreeClassifier()
        clf_dt=self.dt.fit(x_train,y_train)
        
        
        # In[35]:
        
        
        from sklearn import cross_validation
        scores = cross_validation.cross_val_score(self.dt, x_test, y_test, cv=3)


# In[36]:



       
       
               
        
        
    def predict(self,list):
        from sklearn import tree 
        
        
        # #### Finding the Feature importances - From here we need to put it in a function, so we can call it multiple times
        
        # In[37]:
        
        
       
        import numpy as np
        import matplotlib.pyplot as plt
        
        importances = self.dt.feature_importances_
        indices = np.argsort(importances)[::-1]
        features = self.cols
        
        
        # In[38]:
        
        
        feature_dict = {}
        for i,f in enumerate(features):
            feature_dict[f] = i
        
        
        # In[39]:
        
        
        
        x = []
        for symptom in list:
            if(symptom in feature_dict):
                x.append(feature_dict[symptom])
        print(x)
        
        
        # In[40]:
        
        
        sample_x=[]
        for i in range(len(features)):
            if i in x:
                sample_x.append(1.0)
            else:
                sample_x.append(0.0)
        print(sample_x)
        
        
        # In[41]:
        
        
        len(sample_x)
        
        
        # In[42]:
        
        
        sample_x = np.array(sample_x).reshape(1,len(sample_x))
        print(sample_x)
        
        
        # In[43]:
        
        print(self.dt.predict(sample_x))
        return self.dt.predict(sample_x)
        #self.dt.predict_proba(sample_x)
           