#!/usr/local/bin/python3.6

# enable debugging
import cgitb
import cgi
import pandas as pd
import numpy as np
import unicodecsv as csv
import re
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers


print("<TITLE>Spam User detection</TITLE>")
print('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>')
print("""<style>
.loader {
  border: 16px solid #f3f3f3;
  border-radius: 50%;
  border-top: 16px solid #3498db;
  width: 120px;
  height: 120px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

/* Safari */
@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>""")

print("<H1>Please wait while the Spam User file is being generated</H1>")
print('<div class="loader"></div>')

form = cgi.FieldStorage()

def spam_count1(user_id):
        #print(user_id[0])
        count=0
        trial=[]
        for x in range(0, len(spamwords)):
            temp_count=str(user_id[1]).count(str(swords[x]))
            if(temp_count>0):
                trial.append(str(swords[x]))
            count=temp_count+count
        #print(user_id[0],count,trial)
        return (user_id[0],count,trial)
    
def spam_count2(user_id):
    #print(user_id[0])
    count=0
    trial=[]
    for x in range(0, len(spamwords)):
        temp_count=0
        if str(swords[x]) in str(user_id[1]):
            temp_count=1
        else:
            temp_count=0
        if(temp_count>0):
            trial.append(str(swords[x]))
        count=temp_count+count
    #print(user_id[0],count,trial)
    return (user_id[0],count,trial)

def spam_count3(user_id):
    #print(user_id[0])
    count=0
    trial=[]
    for x in range(0, len(spam)):
        temp_count=str(user_id[1]).count(str(spam[x]))
        if(temp_count>0):
            trial.append(str(swords[x]))
        count=temp_count+count
    #print(user_id[0],count,trial)
    return (user_id[0],count,trial)

def spam_count4(user_id):
    #print(user_id[0])
    count=0
    trial=[]
    for x in range(0, len(spam)):
        temp_count=0
        if str(spam[x]) in str(user_id[1]):
            temp_count=1
        else:
            temp_count=0
        if(temp_count>0):
            trial.append(str(swords[x]))
        count=temp_count+count
    #print(user_id[0],count,trial)
    return (user_id[0],count,trial)

def spam_count5(user_id):
    #print(user_id[0])
    count=0
    count=str(user_id[1]).count("http")
    #print(user_id[0],count,trial)
    return (user_id[0],count)

def spam_count6(url):
    #print(user_id[0])
    a=0
    for x in range(0, len(dFn)):
        if(dFn[x]==url):
            a=1
            break;
    return a

def spam_count7(user_id):
    #print(user_id[0])
    count=0
    trial=[]
    for x in range(0, len(temp4)):
        temp_count=0
        if str(temp4[x]) in str(user_id[1]):
            temp_count=1
        else:
            temp_count=0
        if(temp_count>0):
            trial.append(str(temp4[x]))
        count=temp_count+count
    #print(user_id[0],count,trial)
    return (user_id[0],count,trial)

def ngrams(string, n=3):
    string = re.sub(r'[,-./]',r'', string)
    string=string.lower()
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


# In[331]:

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    try:
        check=intersection_cardinality/float(union_cardinality)
    except:
        check=0
    return check


def spam_trap():
    #print(dF)
    from multiprocessing import Pool
    from multiprocessing import Process, Manager
    import time
    # In[259]:
    

    # ## 1) Spamwords
    #print("in")
    # ### 1-a) Spamword Set 1

    # In[260]:
    global spamwords
    spamwords=pd.read_csv("spamwords.csv", index_col=0)


    # In[261]:

    spamwords=spamwords[:447]


    # In[262]:

    spamwords=spamwords.fillna("FREEE")


    # In[263]:
    global swords
    swords=spamwords["spam"].tolist()


    # In[264]:

    temp=dF


    # In[265]:

    temp["setting_value"]=temp["signature"].astype(str)+temp["biography"]
    first=temp["user_id"].tolist()
    second=temp["setting_value"].tolist()
    third=[]
    nan=np.nan
    for x in range(0,len(first)):
        if(second[x] is nan):
            second[x]="0"
        third.append([first[x],second[x]])


    # In[266]:
    #print("in")
    p = Pool(16)
    #print("in")
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    at=p.map(spam_count1,third)
    t1=time.time()
    total=t1-t0
    ##print("Total time",total)


    # In[267]:

    ##print(at)


    # In[268]:

    users=[];
    for x in range(0,len(at)):
        if(len(at[x][2])>0):
            users.append(at[x][0])


    # In[269]:

    score_number_table1=[];
    for x in range(0,len(at)):
        score_number_table1.append(at[x][1])


    # In[270]:



    p = Pool(16)
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    at1=p.map(spam_count2,third)
    t1=time.time()
    total=t1-t0
    #print("Total time",total)
    p.close()


    # In[271]:

    #print(at1)


    # In[272]:

    score_table1=[];
    for x in range(0,len(at1)):
        score_table1.append(at1[x][1])


    # ### 1-b) Spamword Set 2

    # In[273]:

    from bs4 import BeautifulSoup
    import urllib.request
    ra = urllib.request.urlopen("https://blog.hubspot.com/blog/tabid/6307/bid/30684/the-ultimate-list-of-email-spam-trigger-words.aspx")
    r=ra.read()
    soup = BeautifulSoup(r)
    #print(type(soup))
    ##print(soup.prettify()[0:1000000])


    # In[274]:

    import numbers
    #a=soup.table
    trs=soup.findAll('tr')
    #b=a[0].next_element
    ##print(b)
    #i=0;
    global spam
    spam=[]
    tables = soup.findAll("table")

    for table in tables:
        if table.findParent("table") is None:
            a=str(table)
            soup2 = BeautifulSoup(a)
            for row in soup2.find_all("tr")[1:]:  #row by row
                col = row.find_all("td") # differentiating the td into columns.
                col = [ele.text.strip() for ele in col]
                #i=i+1;
                ##print(i)
                try:                     #trying to convert them into strings.
                    spam.append(str(col[0]))
                    spam.append(str(col[1]))
                    spam.append(str(col[2]))
                    #spam.append(str(col[3])) ## I could've put them in a for loop
                    # but then I would have to rewrite the code for try and except
                    da=0
                except OSError as err:
                    #print("OS error: {0}".format(err))
                    da=0
                except ValueError:
                    #print("Expected a string and got something else") 
                    da=0
                except:
                    #print("Unexpected error:", sys.exc_info()[0])
                    raise
                    ##print(col)
                    #print("---")
                ##print(spam)

    ##print(spam)


    # In[275]:

    p = Pool(16)
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    at2=p.map(spam_count3,third)
    t1=time.time()
    total=t1-t0
    #print("Total time",total)
    #print("in")

    # In[276]:

    ##print(at2)


    # In[277]:

    users2=[];
    for x in range(0,len(at2)):
        if(len(at2[x][2])>0):
            users2.append(at2[x][0])


    # In[278]:

    u12=0
    for x in range(0,len(users)):
        for i in range(0, len(users2)):
            if(users[x]==users2[i]):
                u12=u12+1
                break;


    # In[279]:

    score_number_table2=[];
    for x in range(0,len(at2)):
        score_number_table2.append(at2[x][1])


    # In[280]:

    p = Pool(16)
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    at3=p.map(spam_count4,third)
    t1=time.time()
    total=t1-t0
    #print("Total time",total)
    p.close()

    #print("in")
    # In[281]:

    ##print(at3)


    # In[282]:

    score_table2=[];
    for x in range(0,len(at3)):
        score_table2.append(at3[x][1])


    # In[283]:

    dF["score_number_table1"]=score_number_table1
    dF["score_table1"]=score_table1
    dF["score_table2"]=score_table2
    dF["score_number_table2"]=score_number_table2


    # In[284]:

    dF['score_table']=dF['score_table1']+dF['score_table2']
    dF['score_number_table']=dF['score_number_table1']+dF['score_number_table2']


    # ## 2) URLS in the biography and signature

    # In[285]:

    from multiprocessing import Pool
    from multiprocessing import Process, Manager

    p = Pool(16)
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    at4=p.map(spam_count5,third)
    t1=time.time()
    total=t1-t0
    #print("Total time",total)


    # In[286]:

    temp=[]
    for x in range(0,len(at)):
        temp.append(at4[x][1])


    # In[287]:

    dF["links"]=temp


    # In[288]:
    #print("in here")
    #dF["links"].hist()
    bins = np.linspace(0, 10, 40) # Starts with 0, last one is 3, 
    avg=sum(temp)/len(temp)
    #print("The average is", avg,"Max is", max(temp))


    # In[289]:

    #plt.hist(temp,bins, alpha=0.5, histtype='bar')
    #plt.show()


    # In[290]:

    above0=len(dF[dF["links"]>0])
    above1=len(dF[dF["links"]>1])
    #print("more than 0",above0,"more than 1",above1)


    # ### 0 is 0, 1 is 1, >1 is 2

    # In[291]:

    temp_store=[]
    for x in range(0,len(temp)):
        if(temp[x]==0):
            temp_store.append(temp[x])
        elif(temp[x]==1):
            temp_store.append(temp[x])
        else:
            temp_store.append(2)


    # In[292]:

    len(temp_store),max(temp_store),min(temp_store)

    # In[293]:

    #plt.hist(temp_store,bins, alpha=0.5, histtype='bar')
    #plt.show()


    # ## Also, adding the links and setting value which is biography + signature to the dataframe.

    # In[294]:

    dF["setting_value"]=dF["signature"].astype(str)+dF["biography"]
    dF["links"]=temp_store


    # The first table of spam words, the score_number_table1, is the number of times the spam words did occur in that setting_value. The score_table1 is the number of spam words used in the setting_value.
    # 
    # The second table of spam words, the score_number_table2, is the number of times the spam words did occur in that setting_value. The score_table2 is the number of spam words used in the setting_value.

    # ## 3) Regular expressions in the email- regex [a-z,A-z,_-.]+[0-9]
    # 

    # In[295]:
    import re
    emailRegex = re.compile('^[a-zA-Z._-]{3,30}[0-9]{0,4}$', re.VERBOSE)


    # In[296]:

    temp=dF["email"].str.contains('edu',case=False)
    count=0
    temp_store=[]
    for x in range(0,len(dF)):
        user=str(dF["email"].iloc[x])
        user=user.split('@')[0]
        final=re.search(emailRegex, str(user), flags=0)
        if(temp.iloc[x]):
            count=count+1
            temp_store.append(1)
        else:
            if(final!=None):
                count=count+1
                temp_store.append(1)
            else:
                temp_store.append(0)


    # In[297]:

    dF["regex"]=temp_store


    # ## 4) Adding URL's which have been used more than 1 time and do not have edu at the end or .edu. or ends with edu or .edu/

    # In[298]:

    dF['url']=dF['url'].fillna('0')


    # In[299]:
    global dFn
    dFn=dF.groupby(dF["url"]).size().to_frame('count').reset_index()
    dFn=dFn[dFn["count"]>1]
    dFn=dFn.sort_values("count", ascending=False)
    dFn=dFn[dFn["url"].str.contains('http')]
    dFn=dFn[dFn["url"].str.contains('orcid')==False]
    dFn=dFn[dFn["url"].str.contains('.edu.',regex=False)==False]
    dFn=dFn[dFn["url"].str.contains('.edu/',regex=False)==False]
    dFn=dFn[dFn["url"].str.endswith('edu')==False]
    #dFn[dFn["url"].str.contains('edu')]
    dFn=dFn.reset_index()
    dFn=dFn[["url","count"]]
    #print("This is the total",dFn["count"].sum(),"Total number of URLs",len(dFn))
    dFn=dFn["url"].tolist()


    # In[300]:

    urls=dF['url'].tolist()


    # In[301]:

    import time
    import multiprocessing
    from multiprocessing import Pool
    from multiprocessing import Process, Manager

    p = Pool(16)
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    at5=p.map(spam_count6,urls)
    t1=time.time()
    total=t1-t0
    #print("Total time",total)


    # ### Adding the spam urls to the dataframe
    # 

    # In[302]:

    dF["spam_urls"]=at5


    # ## 5) email addresses ending with .edu or has .edu.
    # 

    # In[303]:

    temp=(dF['email'].str.endswith("edu", na=False)) | (dF["url"].str.contains('.edu.',regex=False))


    # In[304]:

    temp=temp.tolist()


    # In[305]:

    at6=[]
    for x in range(0,len(temp)):
        if(temp[x]==True):
            at6.append(1)
        else:
            at6.append(0)


    # In[306]:

    dF["edu_emails"]=at6


    # ## 6) Similar names case: 'first_name' = last_name' OR 'middle_name'='last_name' OR 'middle_name'='first_name'

    # In[307]:

    temp=(dF['first_name']==dF['last_name']) | (dF['middle_name']==dF['last_name']) | (dF['middle_name']==dF['first_name'])


    # In[308]:

    temp=temp.tolist()


    # In[309]:

    at7=[]
    for x in range(0,len(temp)):
        if(temp[x]==True):
            at7.append(1)
        else:
            at7.append(0)


    # In[310]:

    dF["flmname"]=at7


    # ## 7) Scholarly words used in the setting value

    # In[311]:

    dF1=pd.read_csv("term_frequency.csv",encoding = "utf-8",index_col=0)


    # In[312]:

    dF2=pd.read_csv("setting_value.csv")


    # In[313]:

    dF2=dF2[(~dF2.setting_value.isnull()) & (dF2.email.str.contains("edu"))][:100]


    # In[314]:

    temp=dF2.setting_value.str.split(expand=True).stack().value_counts()


    # In[315]:

    right_words1=[]
    right_words2=[]
    for x in range(0,len(temp)):
        ##print(x)
        for i in range(1,len(dF1)):
            ##print(str(dF1.column.loc[i]),str(temp.index[x]))
            if(str(dF1.column.loc[i])==str(temp.index[x])):
                ##print("do nothing")
                break;
            if(i==(len(dF1)-1)):
                right_words1.append(temp[x])
                right_words2.append(temp.index[x])
                ##print(str(temp.index[x]))


    # In[316]:

    d = {'total_count': right_words1, 'value': right_words2}


    # In[317]:

    temp2=pd.DataFrame(data=d) 


    # In[318]:

    temp2["value"]=temp2["value"].str.replace("nan","")
    temp2["value"]=temp2["value"].str.replace(".","")
    temp2["value"]=temp2["value"].str.replace(",","")
    temp2["value"]=temp2["value"].str.replace('"',"")


    # In[319]:
    global temp4
    temp3=temp2.groupby("value").sum()
    temp4=temp3[temp3["total_count"]>4].sort_values("total_count")
    temp4=temp4.reset_index()


    # In[320]:

    temp4


    # In[321]:

    #temp4.to_csv("actual_words.csv")


    # In[322]:

    temp4=temp4["value"].tolist()


    # ### Filtering the high frequency words by removing the most commonly used words.

    # In[323]:

    dF2=dF


    # In[324]:

    first=dF2["user_id"].tolist()
    second=dF2["setting_value"].tolist()
    third=[]
    nan=np.nan
    for x in range(0,len(first)):
        if(second[x] is nan):
            second[x]="0"
        third.append([first[x],second[x]])


    # In[325]:

    len(third)


    # In[326]:

    import time
    import multiprocessing
    from multiprocessing import Pool
    from multiprocessing import Process, Manager

    p = Pool(16)
    #list_val=temp[["user_id","setting_value"]].tolist()
    t0=time.time()
    ##print(third)
    at3=p.map(spam_count7,third)
    t1=time.time()
    total=t1-t0
    #print("Total time",total)
    p.close()


    # In[327]:

    arr=[]

    for x in range(0,len(at3)):
        if((at3[x][1])>0):
            arr.append(1)
        else:
            arr.append(0)


    # In[328]:

    dF2["score_truth_table"]=arr


    # In[329]:

    dF["score_truth_table"]=dF2["score_truth_table"]


    # ## 8) Jaccard distance with n-grams set to 3

    # In[330]:


    # In[332]:

    temp=dF


    # ### First name and Last name with username

    # In[333]:

    temp["given_name"]=temp["first_name"].astype(str)+temp["last_name"]


    # In[334]:

    arr=[]

    for x in range(0, len(temp)):
        a=str(temp.iloc[x].given_name)
        a=ngrams(a)
        b=str(temp.iloc[x].username)
        b=ngrams(b)
        ##print(a,b)
        arr.append(jaccard_similarity(a,b))    


    # In[335]:

    temp["jaccard"]=arr


    # ### First name and last name with email before @

    # In[336]:

    temp["email"]=temp.email.str.extract("(.*)@")


    # In[337]:

    arr2=[]

    for x in range(0, len(temp)):
        a=str(temp.iloc[x].given_name)
        a=ngrams(a)
        b=str(temp.iloc[x].email)
        b=ngrams(b)
        ##print(a,b)
        arr2.append(jaccard_similarity(a,b))


    # In[338]:

    temp["jaccard2"]=arr2


    # ### Username and email

    # In[339]:

    arr3=[]

    for x in range(0, len(temp)):
        a=str(temp.iloc[x].username)
        a=ngrams(a)
        b=str(temp.iloc[x].email)
        b=ngrams(b)
        ##print(a,b)
        arr3.append(jaccard_similarity(a,b))


    # In[340]:

    temp["jaccard3"]=arr3


    # In[341]:

    temp["jaccard_final"]=(temp["jaccard"]<0.1) & (temp["jaccard2"]<0.1) & (temp["jaccard3"]<0.1)


    # In[342]:

    temp["jaccard_final"]=temp["jaccard_final"].astype(int)


    # In[343]:

    dF["jaccard_final"]=temp["jaccard_final"]


    # # The condition to be run

    # In[344]:

    spammers=dF[
        ((dF["edu_emails"]==0) 
        & ((dF["jaccard_final"]==1)|(dF["flmname"]==1))
        & ((dF["regex"]==0)|dF["links"]>0)) 
        & ((dF["links"]>0)|(dF["spam_urls"]==1) 
           | ((dF["score_table"]==1)
              & (dF["score_truth_table"]==0)))
    ]


    # In[345]:

    spammers
     
    
    # In[346]:
    import datetime
    import time
    import csv
    path='/var/www/html/uni/'
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    st_spam=str(st)+"spam.csv"
    spammers.to_csv(path+st_spam)
    full_path=path+st_spam
    spammers.to_csv(full_path)
    alt_path1='/uni/'
    alt_path2=st_spam
    alt_path=alt_path1+alt_path2
    print("Completed generation of csv file")
    print("<script>")
    print('$(".loader").hide(500)')
    print("</script>")
    print('<a class="downloadLink" href="',alt_path,'" download>Download your file</a>')
    print("<script>")
    print("""$(".downloadLink").click(
    function(e) {   
        e.preventDefault();

        //open download link in new page
        window.open( $(this).attr("href") );

        //redirect current page to success page
        window.location="/index.html";
        window.focus();
    }
    );""")
    print("</script>")
    # In[347]:

    print("The total number of users",len(dF))


    # In[348]:

    len(spammers)
    print("The total number of spam users",len(spammers))


    # In[349]:

    print("The number of true users:",len(dF)-len(spammers))

    # In[350]:

    #33955


    # In[357]:

    #spammers[spammers["user_id"]==12645]
    #print("Completed generation of csv file")


if(not form):
    print('<form action="/cgi-bin/spam_trap.py" method="POST" enctype="multipart/form-data">')
    print('<input type="file" name="CSV">')
    print('<input type="submit">')
    print('</form>')
elif("CSV" in form):
    print('<p>%s : </p>'%form['CSV'].filename)
    print("<table>")
    reader = csv.reader(form['CSV'].file)
    global dF
    dF=pd.read_csv(form['CSV'].file)
    print("CSV file loaded")
    print("Please wait for 2-3 minutes while we generate the spam users")
    spam_trap()
