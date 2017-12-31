class Project:
    def __init__(self,title,agency,boss,price,tax,bonus,costforcode,costforweb,costformanager,costforexpress,costforserver,costforcdn,costformaintenance,costfor3rdparty,manager,flow,prototype,sow,sob,expressno,debugdate,deadline,contract,invoice,getmoney,close,info):
        self.title=title
        self.agency=agency
        self.boss=boss
        self.price=price
        self.tax=tax
        self.bonus=bonus
        self.costforcode=costforcode
        self.costforweb=costforweb
        self.costformanager=costformanager
        self.costforexpress=costforexpress
        self.costforserver=costforserver
        self.costforcdn=costforcode
        self.costformaintenance=costformaintenance
        self.costfor3rdparty=costfor3rdparty
        self.manager=manager
        self.flow=flow
        self.prototype=prototype
        self.sow=sow
        self.sob=sob
        self.expressno=expressno
        self.debugdate=debugdate
        self.deadline=deadline
        self.contract=contract
        self.invoice=invoice
        self.getmoney=getmoney
        self.close=close
        self.info=info

    def __str__(self):
        return f'项目名字是{self.title}'


class H5:
    def __init__(self,webtitle,headline,icon,summary,music,loading,psd,share,data,url,api,monitor,duration,cdn,authorization,multilink,maintenance,h5info):
        self.webtitle=webtitle
        self.headline=headline
        self.summary=summary
        self.icon=icon
        self.music
        self.loading=loading
        self.psd=psd
        self.share=share
        self.data=data
        self.url=url
        self.api=api
        self.monitor=monitor
        self.duration=duration
        self.cdn=cdn
        self.authorization=authorization
        self.multilink=multilink
        self.maintenance=maintenance
        self.info=info




