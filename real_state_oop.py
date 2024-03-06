from tkinter import *
from tkinter import ttk
import sqlite3


class Real_state(Tk):
    def create_database(self):

        self.my_cursor.execute('CREATE TABLE IF NOT EXISTS house_for_sale(Type INTEGER,Area INTEGER,Num_of_rooms INTEGER,Price_per_meter REAL,Total_price REAL,Deposit REAL,Monthly_rents REAL,Zone INTEGER,district TEXT,Full_addres TEXT,Floor INTEGER,Unit INTEGER,Product_year INTEGER,Cabinet_type TEXT,Floor_material TEXT,option_basement TEXT,option_garage TEXT,option_elevator TEXT)')
        self.conector.commit()

    def __init__(self):
        Tk.__init__(self)
        self.geometry('178x120+400+250')
        self.title('Real estates')


        self.conector=sqlite3.connect('real_state_data_base.db')
        self.my_cursor=self.conector.cursor()

        self.btn_add=Button(self,text='add item',font=('Times New Roman',20),width=14,command=self.add_item)
        self.btn_add.grid(row=0,column=0)
        self.btn_search=Button(self,text='search item',font=('Times New Roman',20),width=14,command=self.search_item)
        self.btn_search.grid(row=1,column=0)
        self.btn_updel=Button(self,text='update/delete item',font=('Times New Roman',20),width=14,command=self.update_delet_item)
        self.btn_updel.grid(row=2,column=0)

        self.m=Menu(self)
        self.menu=Menu(self.m,tearoff=0)
        self.menu.add_command(label='add item',command=self.add_item)
        self.menu.add_command(label='search item',command=self.search)
        self.menu.add_command(label='update/delete item',command=self.update_delet_item)
        self.menu.add_separator()
        self.menu.add_command(label='quit',command=lambda:self.destroy())
        self.m.add_cascade(label='actions',menu=self.menu)

        self.menu2=Menu(self.m)
        self.menu2.add_command(label='dark',command=self.dark_theme)
        self.menu2.add_command(label='light',command=self.light_theme)
        self.m.add_cascade(label='theme',menu=self.menu2)
        self.config(menu=self.m)

    def rent_buy_add(self):

    
        if self.rdt_val.get()==1:
            self.type='rent'
            self.entr3.delete(0,END)
            self.entr3.config(state='disable')       
            self.entr5.config(state='normal')
            self.entr6.config(state='normal')
        elif self.rdt_val.get()==2:
            self.type='buy'
            self.entr5.delete(0,END)
            self.entr6.delete(0,END)
            self.entr5.config(state='disable')
            self.entr6.config(state='disable')
            self.entr3.config(state='normal')

    def rent_buy_search(self):

    
        if self.rdt_val.get()==1:
            self.entr5.delete(0,END)
            self.entr6.delete(0,END)
            self.entr7.delete(0,END)
            self.entr8.delete(0,END)
            self.entr5.config(state='disable')        
            self.entr6.config(state='disable')
            self.entr7.config(state='disable')
            self.entr8.config(state='disable')
            self.entr9.config(state='normal')        
            self.entr10.config(state='normal')
            self.entr11.config(state='normal')
            self.entr12.config(state='normal')
        elif self.rdt_val.get()==2:
            self.entr9.delete(0,END)
            self.entr10.delete(0,END)
            self.entr11.delete(0,END)
            self.entr12.delete(0,END)
            self.entr8.config(state='normal')        
            self.entr9.config(state='disable')
            self.entr10.config(state='disable')
            self.entr11.config(state='disable')
            self.entr12.config(state='disable')        
            self.entr5.config(state='normal')
            self.entr6.config(state='normal')
            self.entr7.config(state='normal')

    def rent_buy_delet(self):
        if self.rdt_val.get()==1:
            self.entr4.delete(0,END)
            self.entr5.delete(0,END)
            self.entr4.config(state='disable')
            self.entr5.config(state='disable')        
            self.entr6.config(state='normal')
            self.entr7.config(state='normal')
        elif self.rdt_val.get()==2:
            self.entr5.delete(0,END)
            self.entr6.delete(0,END)
            self.entr6.config(state='disable')
            self.entr7.config(state='disable')
            self.entr4.config(state='normal')
            self.entr5.config(state='normal')

    def rent_buy_delet_file(self):
        if self.rdt_val.get()==1:
            self.entr4.delete(1.0,END)
            self.entr5.delete(1.0,END)
            self.entr4.config(state='disable')
            self.entr5.config(state='disable')        
            self.entr6.config(state='normal')
            self.entr7.config(state='normal')
        elif self.rdt_val.get()==2:
            self.entr6.delete(1.0,END)
            self.entr7.delete(1.0,END)
            self.entr6.config(state='disable')
            self.entr7.config(state='disable')
            self.entr4.config(state='normal')
            self.entr5.config(state='normal')

    def cabinet_delet(self):
        if self.cabinet_val==1:
            return 'None'
        elif self.cabinet_val==2:
            return 'MDF'
        elif self.cabinet_val==3:
            return 'Chipboard'
        elif self.cabinet_val==4:
            return 'High glass'
   
    def cabinet(self):
        if self.cabinet_val.get()==1:
            self.cabinet_type='None'
        elif self.cabinet_val.get()==2:
            self.cabinet_type= 'MDF'
        elif self.cabinet_val.get()==3:
            self.cabinet_type= 'Chipboard'
        elif self.cabinet_val.get()==4:
            self.cabinet_type= 'High glass'
    
    def floor(self):
        if self.floor_val.get()==1:
            self.floor_type= 'None'
        if self.floor_val.get()==2:
            self.floor_type= 'Ceramic'
        if self.floor_val.get()==3:
            self.floor_type= 'Parquat'
        if self.floor_val.get()==4:
            self.floor_type= 'Mosaic'

    def option(self):
        if self.option_val_bass.get()==1:
            self.option_basement='Basement'
        else:
            self.option_basement=' '

        if self.option_val_garage.get()==1:
            self.option_garage='Garage'
        else:
            self.option_garage=' '

        if self.option_val_elevator.get()==1:
            self.option_elevator='Elevator'
        else:
            self.option_elevator=' '
  
    def loc_zone_add(self,x):
        
        self.zone_1=['zaferanie','velenjak','ozgol','evin','tajrish','gheytarie','farmanie','niyavaran']
        self.zone_2=['saadat abad','shahrak gharb','aria shahr','gisha','marzdaran','tarasht']
        self.zone_3=['vanak','gholhak','mirdamad','darus']
        self.zone_4=['tehranpars','hakimie','shams abad','pasdara','narmak','lavizan']
        self.zone_5=['shahran','ekbatan','punak','janat abad']
        self.zone_6=['jahad','sanaei','yusef abad']
        self.zone_7=['nezam abad','enghelab','ferdosi','seyed khandan']
        self.zone_8=['narmak','hafthoz','dardasht','fadak']
        self.zone_9=['mehrabad','shamshiri','sarasiab','fath']
        self.zone_10=['7chenar','berianak','J','salsabil']
        self.zone_11=['hafez','karegar','valiasr','emam khomeini','jomhuri','monirie','ghazvin']
        self.zone_12=['darvaze shemiran','pamenar','baharestan','ferdosi']
        self.zone_13=['piruzi','niru havaei','tehran no','shokufe']
        self.zone_14=['dulab','sarasiab','ghasr firuze','sad dastgah']
        self.zone_15=['kianshahr','afsarie','masudie','moshirie','khavaran']
        self.zone_16=['javadie','naziabad','yakhchiabad','khazane','besat']
        self.zone_17=['azari','yaftabad','blur sazi','abuzar']
        self.zone_18=['ferdos','sadeghie','behdasht','rajaei']
        self.zone_19=['khani abad','shokufe','velayat','bahmanyar']
        self.zone_20=['javanmard ghasab','deylaman','hamze abad','firuz abadi']
        self.zone_21=['vard avard','tehransar','chitgar','ghazali','daneshgah']
        self.zone_22=['dehkade olampic','ziba dasht','shahrak cheshme','shahrak sadra']

        if self.zone.get()=='1':
            self.drp_ds.config(values=self.zone_1,state='normal')
        elif self.zone.get()=='2':
            self.drp_ds.config(values=self.zone_2,state='normal')
        elif self.zone.get()=='3':
            self.drp_ds.config(values=self.zone_3,state='normal')
        elif self.zone.get()=='4':
            self.drp_ds.config(values=self.zone_4,state='normal')
        elif self.zone.get()=='5':
            self.drp_ds.config(values=self.zone_5,state='normal')
        elif self.zone.get()=='6':
            self.drp_ds.config(values=self.zone_6,state='normal')
        elif self.zone.get()=='7':
            self.drp_ds.config(values=self.zone_7,state='normal')
        elif self.zone.get()=='8':
            self.drp_ds.config(values=self.zone_8,state='normal')
        elif self.zone.get()=='9':
            self.drp_ds.config(values=self.zone_9,state='normal')
        elif self.zone.get()=='10':
            self.drp_ds.config(values=self.zone_10,state='normal')
        elif self.zone.get()=='11':
            self.drp_ds.config(values=self.zone_11,state='normal')
        elif self.zone.get()=='12':
            self.drp_ds.config(values=self.zone_12,state='normal')
        elif self.zone.get()=='13':
            self.drp_ds.config(values=self.zone_13,state='normal')
        elif self.zone.get()=='14':
            self.drp_ds.config(values=self.zone_14,state='normal')
        elif self.zone.get()=='15':
            self.drp_ds.config(values=self.zone_15,state='normal')
        elif self.zone.get()=='16':
            self.drp_ds.config(values=self.zone_16,state='normal')
        elif self.zone.get()=='17':
            self.drp_ds.config(values=self.zone_17,state='normal')
        elif self.zone.get()=='18':
            self.drp_ds.config(values=self.zone_18,state='normal')
        elif self.zone.get()=='19':
            self.drp_ds.config(values=self.zone_19,state='normal')
        elif self.zone.get()=='20':
            self.drp_ds.config(values=self.zone_20,state='normal')
        elif self.zone.get()=='21':
            self.drp_ds.config(values=self.zone_21,state='normal')
        elif self.zone.get()=='22':
            self.drp_ds.config(values=self.zone_22,state='normal')

    def show_file(self):

        self.delete_w=Toplevel(self)
        self.delete_w.title('Files')
        self.delete_w.geometry('1000x600')

        self.txt=Text(self.delete_w,border=3,relief='solid')
        self.txt.pack(expand=True,fill='both')

        
        self.my_cursor.execute('SELECT rowid,* FROM house_for_sale')
        show=self.my_cursor.fetchall()
        for i in show:
            self.txt.insert(END,i)
            self.txt.insert(END,'\n')

    def add_item(self):

        self.add_w=Toplevel(self)
        self.add_w.title('add item')
        self.add_w.geometry('1000x600+600+250')

        self.m=Menu(self.add_w)
        self.menu=Menu(self.m,tearoff=0)
        self.menu.add_command(label='add item',command=self.add_item)
        self.menu.add_command(label='search item',command=self.search)
        self.menu.add_command(label='update/delete item',command=lambda:print('delet'))
        self.menu.add_separator()
        self.menu.add_command(label='quit',command=self.update_delet_item)
        self.m.add_cascade(label='actions',menu=self.menu)

        self.menu2=Menu(self.m)
        self.menu2.add_command(label='dark',command=self.dark_theme_add)
        self.menu2.add_command(label='light',command=self.light_theme_add)
        self.m.add_cascade(label='theme',menu=self.menu2)
        self.config(menu=self.m)
    

        self.lbl1=Label(self.add_w,text='Type:',font=('Times New Roman',20))
        self.lbl2=Label(self.add_w,text='Area:',font=('Times New Roman',20))
        self.lbl3=Label(self.add_w,text='Num of rooms:',font=('Times New Roman',20))
        self.lbl4=Label(self.add_w,text='Price per meter:',font=('Times New Roman',20))
        self.lbl5=Label(self.add_w,text='Total price:',font=('Times New Roman',20))
        self.lbl6=Label(self.add_w,text='Deposit:',font=('Times New Roman',20))
        self.lbl7=Label(self.add_w,text='Monthly rents:',font=('Times New Roman',20))
        self.lbl8=Label(self.add_w,text='Address:',font=('Times New Roman',20))
        self.lbl9=Label(self.add_w,text='Full address:',font=('Times New Roman',20))
        self.lbl10=Label(self.add_w,text='Floor:',font=('Times New Roman',20))
        self.lbl11=Label(self.add_w,text='Unit:',font=('Times New Roman',20))
        self.lbl12=Label(self.add_w,text='Product year:',font=('Times New Roman',20))
        self.lbl13=Label(self.add_w,text='Cabinet type:',font=('Times New Roman',20))
        self.lbl14=Label(self.add_w,text='Floor material:',font=('Times New Roman',20))
        self.lbl15=Label(self.add_w,text='Other options:',font=('Times New Roman',20))
        self.entr4=Label(self.add_w,width=60,border=3,relief='solid')


        self.lbl1.grid(row=0,column=0,sticky='w')
        self.lbl2.grid(row=1,column=0,sticky='w')
        self.lbl3.grid(row=2,column=0,sticky='w')
        self.lbl4.grid(row=3,column=0,sticky='w')
        self.lbl5.grid(row=4,column=0,sticky='w')
        self.lbl6.grid(row=5,column=0,sticky='w')
        self.lbl7.grid(row=6,column=0,sticky='w')
        self.lbl8.grid(row=7,column=0,sticky='w')
        self.lbl9.grid(row=8,column=0,sticky='w')
        self.lbl10.grid(row=9,column=0,sticky='w')
        self.lbl11.grid(row=9,column=2,sticky='w')
        self.lbl12.grid(row=9,column=4,sticky='w')
        self.lbl13.grid(row=10,column=0,sticky='w')
        self.lbl14.grid(row=12,column=0,sticky='w')
        self.lbl15.grid(row=14,column=0,sticky='w')
        self.entr4.grid(row=4,column=1,columnspan=5)


        self.entr1=Entry(self.add_w,width=60,border=3,relief='solid')
        self.entr2=Entry(self.add_w,width=60,border=3,relief='solid')
        self.entr3=Entry(self.add_w,width=60,state='disabled',border=3,relief='solid')
        self.entr5=Entry(self.add_w,width=60,state='disabled',border=3,relief='solid')
        self.entr6=Entry(self.add_w,width=60,state='disabled',border=3,relief='solid')
        self.entr7=Entry(self.add_w,width=60,border=3,relief='solid')
        self.entr9=Entry(self.add_w,border=3,relief='solid')
        self.entr8=Entry(self.add_w,border=3,relief='solid')


        self.entr1.grid(row=1,column=1,columnspan=5)
        self.entr2.grid(row=2,column=1,columnspan=5)
        self.entr3.grid(row=3,column=1,columnspan=5)
        self.entr5.grid(row=5,column=1,columnspan=5)
        self.entr6.grid(row=6,column=1,columnspan=5)
        self.entr7.grid(row=8,column=1,columnspan=5)
        self.entr9.grid(row=9,column=1)
        self.entr8.grid(row=9,column=3)



        # rent buy
        self.rdt_val=IntVar()
        self.rdt1=Radiobutton(self.add_w,text='Rent',variable=self.rdt_val,value=1,command=self.rent_buy_add)
        self.rdt2=Radiobutton(self.add_w,text='Buy',variable=self.rdt_val,value=2,command=self.rent_buy_add)
        # cabinet type
        self.cabinet_val=IntVar()
        self.rdt4=Radiobutton(self.add_w,text='None',variable=self.cabinet_val,value=1,command=self.cabinet)
        self.rdt5=Radiobutton(self.add_w,text='MDF',variable=self.cabinet_val,value=2,command=self.cabinet)
        self.rdt6=Radiobutton(self.add_w,text='Chipboard',variable=self.cabinet_val,value=3,command=self.cabinet)
        self.rdt7=Radiobutton(self.add_w,text='High glass',variable=self.cabinet_val,value=4,command=self.cabinet)
        #floor material
        self.floor_val=IntVar()
        self.rdt8=Radiobutton(self.add_w,text='None',variable=self.floor_val,value=1,command=self.floor)
        self.rdt9=Radiobutton(self.add_w,text='Ceramic',variable=self.floor_val,value=2,command=self.floor)
        self.rdt10=Radiobutton(self.add_w,text='Parquet',variable=self.floor_val,value=3,command=self.floor)
        self.rdt11=Radiobutton(self.add_w,text='Mosaic',variable=self.floor_val,value=4,command=self.floor)
        # other option
        self.option_val_bass=IntVar()
        self.option_val_garage=IntVar()
        self.option_val_elevator=IntVar()
        self.rdt12=Checkbutton(self.add_w,text='Basement',variable=self.option_val_bass,onvalue=1,offvalue=0,command=self.option)
        self.rdt13=Checkbutton(self.add_w,text='Garage',variable=self.option_val_garage,onvalue=1,offvalue=0,command=self.option)
        self.rdt14=Checkbutton(self.add_w,text='Elevator',variable=self.option_val_elevator,onvalue=1,offvalue=0,command=self.option)

        self.rdt1.grid(row=0,column=2)
        self.rdt2.grid(row=0,column=3)
        self.rdt4.grid(row=11,column=0)
        self.rdt5.grid(row=11,column=1)
        self.rdt6.grid(row=11,column=2)
        self.rdt7.grid(row=11,column=3)
        self.rdt8.grid(row=13,column=0)
        self.rdt9.grid(row=13,column=1)
        self.rdt10.grid(row=13,column=2)
        self.rdt11.grid(row=13,column=3)
        self.rdt12.grid(row=15,column=0)
        self.rdt13.grid(row=15,column=1)
        self.rdt14.grid(row=15,column=2)


        # addres drop down
        self.zone=StringVar()
        self.zone_val=[i for i in range(1,23)]
        self.zone.set('zone')
        self.drp_zn=ttk.Combobox(self.add_w,values=self.zone_val,textvariable=self.zone)
        self.drp_zn.grid(row=7,column=1,sticky='e',columnspan=2)
        self.drp_zn.bind("<<ComboboxSelected>>",self.loc_zone_add)    

        self.district=StringVar()
        self.district.set('district')  
        self.drp_ds=ttk.Combobox(self.add_w,textvariable=self.district,state='disable')
        self.drp_ds.grid(row=7,column=3,sticky='e',columnspan=2)


        # product year

        self.pr_year=StringVar()
        self.pr_year.set('year')
        self.pr_val=[i for i in range(1340,1404)]
        self.drp_pr=ttk.Combobox(self.add_w,values=self.pr_val,textvariable=self.pr_year)
        self.drp_pr.grid(row=9,column=5)

        self.btn1=Button(self.add_w,text='add',font=('Times New Roman',20),width=70,command=self.add)
        self.btn1.grid(row=16,column=0,columnspan=6)

    def add(self):
        try:
            type=False
            area=False
            rooms=False
            price=False
            diposit=False
            rent=False
            f_addres=False
            floor=False
            unit=False
            zone=False
            district=False
            year=False
            cabinet=False
            floor_mat=False

            
        # type rent buy
            try:
                if self.rdt_val.get()==1:
                    type=True
                    pass
                elif self.rdt_val.get()==2:
                    type=True
                    pass
                else:
                    raise TypeError
            except TypeError:
                print('please select a "Type"')
                type=False

        # area
                
            try:
                if len(self.entr1.get())>0 and self.entr1.get().isdigit():
                    area=True
                else:
                    raise TypeError
            except TypeError:
                print('please insert "area" of your house!')
                area=False

        # num of rooms
            
            try:
                if len(self.entr2.get())>0 and self.entr2.get().isdigit():
                    rooms=True
                else:
                    raise TypeError
            except TypeError:
                print('please insert "number of rooms" of your house!')
                rooms=False

        # price per meter
            try:
                if self.rdt_val.get()==2:
                    if len(self.entr3.get())>0 and self.entr3.get().isdigit():
                        #self.entr4.config(state='disable')
                        self.total_price=int(self.entr3.get())*int(self.entr1.get())
                        self.entr4.config(text=f"{self.total_price}")
                        price=True
                        diposit=True
                        rent=True
                    else:
                        raise TypeError
            except TypeError:
                print('please insert "price per meter" of your house!')
                price=False


            # deposit
            try:
                if self.rdt_val.get()==1:
                    if len(self.entr5.get())>0 and self.entr5.get().isdigit() or "." in self.entr5.get():
                        diposit=True
                        price=True
                    else:
                        raise TypeError
            except TypeError:
                print('please insert "deposit" of your house!')
                diposit=False

            # rent
                
            try:
                if self.rdt_val.get()==1:
                    if len(self.entr6.get())>0 and self.entr6.get().isdigit() or  "." in self.entr6.get():
                        rent=True
                        price=True
                    else:
                        raise TypeError
            except TypeError:
                print('please insert "monthly rent" of your house!')
                rent=False
                
            # full addres
                
            try:
                if len(self.entr7.get())>0 :
                    f_addres=True
                else:
                    raise TypeError
            except TypeError:
                print('please insert the "address" of your house!')
                f_addres=False

            # floor
            try:
                if len(self.entr9.get())>0 and self.entr9.get().isdigit():
                    floor=True
                else:
                    raise TypeError
            except TypeError:
                print('please insert "floor" of your house!')
                floor=False

            # unit
                
            try:
                if len(self.entr8.get())>0 and self.entr8.get().isdigit():
                    unit=True
                else:
                    raise TypeError
            except TypeError:
                print('please insert "unit" of your house!')
                unit=False

            # zone
            
            try:
                if self.zone.get()=='zone' or self.zone.get()=='':
                    raise TypeError
                    zone=False
                else:
                    zone=True
            except TypeError:
                print('please select the "zone"')
                
            # district
                
            try:
                if self.district.get()=='district' or self.district.get()=='':
                    raise TypeError
                    district=False
                else:
                    district=True
            except TypeError:
                print('please select the "district"')

            # year
            try:
                if self.pr_year.get()=='year' or self.pr_year.get()=='':
                    raise TypeError
                    year=False
                else:
                    year=True
            except TypeError:
                print('please select the "year"')    

            # cabinet

            try:
                if self.cabinet_val.get()==1 or self.cabinet_val.get()==2 or self.cabinet_val.get()==3 or self.cabinet_val.get()==4:
                    cabinet=True
                else:
                    cabinet=False
                    raise TypeError
            except TypeError:
                print('please choice one of the "cabinet type"')

            # floor material
            try:
                if self.floor_val.get()==1 or self.floor_val.get()==2 or self.floor_val.get()==3 or self.floor_val.get()==4:
                    floor_mat=True
                else:
                    floor_mat=False
                    raise TypeError
            except TypeError:
                print('please choice one of the "floor material"')






            file=[self.type,self.entr1.get(),self.entr2.get(),self.entr3.get(),self.entr4.cget("text"),self.entr5.get(),self.entr6.get(),self.zone.get(),self.district.get(),self.entr7.get(),self.entr9.get(),self.entr8.get(),self.pr_year.get(),self.cabinet_type,self.floor_type,self.option_basement,self.option_garage,self.option_elevator]
            
            if type==True and area==True and rooms==True and price==True and diposit==True and rent==True and f_addres==True and floor==True and unit==True and zone==True and district==True and year==True and cabinet==True and floor_mat==True:
                self.my_cursor.execute('INSERT OR IGNORE INTO house_for_sale(Type,Area,Num_of_rooms,Price_per_meter,Total_price,Deposit,Monthly_rents,Zone,district,Full_addres,Floor,Unit,Product_year,Cabinet_type,Floor_material,option_basement,option_garage,option_elevator) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',file)
                self.conector.commit()
        except:
            print('enter your home information')

    def search_item(self):

        self.search_w=Toplevel(self)
        self.search_w.title('search item')
        self.search_w.geometry('460x500+600+250')

        self.m=Menu(self.search_w)
        self.menu=Menu(self.m,tearoff=0)
        self.menu.add_command(label='add item',command=self.add_item)
        self.menu.add_command(label='search item',command=self.search)
        self.menu.add_command(label='update/delete item',command=self.update_delet_item)
        self.menu.add_separator()
        self.menu.add_command(label='quit',command=lambda:self.destroy())
        self.m.add_cascade(label='actions',menu=self.menu)

        self.menu2=Menu(self.m)
        self.menu2.add_command(label='dark',command=self.dark_theme_search)
        self.menu2.add_command(label='light',command=self.light_theme_search)
        self.m.add_cascade(label='theme',menu=self.menu2)
        self.config(menu=self.m)

        self.lbl1=Label(self.search_w,text='Type:',font=('Times New Roman',20))
        self.lbl2=Label(self.search_w,text='Area(m):',font=('Times New Roman',20))
        self.lbl3=Label(self.search_w,text='Num of rooms:',font=('Times New Roman',20))
        self.lbl4=Label(self.search_w,text='Price per meter:',font=('Times New Roman',20))
        self.lbl5=Label(self.search_w,text='Total price:',font=('Times New Roman',20))
        self.lbl6=Label(self.search_w,text='Deposit:',font=('Times New Roman',20))
        self.lbl7=Label(self.search_w,text='Monthly rents:',font=('Times New Roman',20))
        self.lbl8=Label(self.search_w,text='Address:',font=('Times New Roman',20))
        self.lbl9=Label(self.search_w,text='Product year:',font=('Times New Roman',20))
        self.lbl10=Label(self.search_w,text='Floor:',font=('Times New Roman',20))
        self.lbl11=Label(self.search_w,text='Unit:',font=('Times New Roman',20))
        self.lbl12=Label(self.search_w,text='Cabinet type:',font=('Times New Roman',20))
        self.lbl13=Label(self.search_w,text='Floor material:',font=('Times New Roman',20))
        self.lbl14=Label(self.search_w,text='Other options:',font=('Times New Roman',20))

        self.lbl1.grid(row=0,column=0,sticky='w')
        self.lbl2.grid(row=1,column=0,sticky='w')
        self.lbl3.grid(row=2,column=0,sticky='w')
        self.lbl4.grid(row=3,column=0,sticky='w')
        self.lbl5.grid(row=4,column=0,sticky='w')
        self.lbl6.grid(row=5,column=0,sticky='w')
        self.lbl7.grid(row=6,column=0,sticky='w')
        self.lbl8.grid(row=7,column=0,sticky='w')
        self.lbl9.grid(row=8,column=0,sticky='w')
        self.lbl10.grid(row=9,column=0,sticky='w')
        self.lbl11.grid(row=9,column=2)
        self.lbl12.grid(row=10,column=0,sticky='w')
        self.lbl13.grid(row=12,column=0,sticky='w')
        self.lbl14.grid(row=14,column=0,sticky='w')

        self.entr1=Entry(self.search_w,width=10,border=3,relief='solid')
        self.entr2=Entry(self.search_w,width=10,border=3,relief='solid')
        self.entr3=Entry(self.search_w,width=10,border=3,relief='solid')
        self.entr4=Entry(self.search_w,width=10,border=3,relief='solid')
        self.entr5=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr6=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr7=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr8=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr9=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr10=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr11=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr12=Entry(self.search_w,width=10,border=3,relief='solid',state='disabled')
        self.entr13=Entry(self.search_w,width=10,border=3,relief='solid')
        self.entr14=Entry(self.search_w,width=10,border=3,relief='solid')
   

        self.entr1.grid(row=1,column=1,sticky='w',columnspan=2)
        self.entr2.grid(row=1,column=3,sticky='w',columnspan=2)
        self.entr3.grid(row=2,column=1,sticky='w',columnspan=2)
        self.entr4.grid(row=2,column=3,sticky='w',columnspan=2)
        self.entr5.grid(row=3,column=1,sticky='w',columnspan=2)
        self.entr6.grid(row=3,column=3,sticky='w',columnspan=2)
        self.entr7.grid(row=4,column=1,sticky='w',columnspan=2)
        self.entr8.grid(row=4,column=3,sticky='w',columnspan=2)
        self.entr9.grid(row=5,column=1,sticky='w',columnspan=2)
        self.entr10.grid(row=5,column=3,sticky='w',columnspan=2)
        self.entr11.grid(row=6,column=1,sticky='w',columnspan=2)
        self.entr12.grid(row=6,column=3,sticky='w',columnspan=2)
        self.entr13.grid(row=9,column=1,sticky='w')
        self.entr14.grid(row=9,column=3,sticky='w')


        # rent buy
        self.rdt_val=IntVar()
        self.rdt1=Radiobutton(self.search_w,text='Rent',variable=self.rdt_val,value=1,indicatoron=0,command=self.rent_buy_search)
        self.rdt2=Radiobutton(self.search_w,text='Buy',variable=self.rdt_val,value=2,indicatoron=0,command=self.rent_buy_search)
        self.rdt1.grid(row=0,column=1)
        self.rdt2.grid(row=0,column=3)

        # cabinet type
        self.cabinet_val=IntVar()
        self.rdt4=Radiobutton(self.search_w,text='None',variable=self.cabinet_val,value=1,command=self.cabinet)
        self.rdt5=Radiobutton(self.search_w,text='MDF',variable=self.cabinet_val,value=2,command=self.cabinet)
        self.rdt6=Radiobutton(self.search_w,text='Chipboard',variable=self.cabinet_val,value=3,command=self.cabinet)
        self.rdt7=Radiobutton(self.search_w,text='High glass',variable=self.cabinet_val,value=4,command=self.cabinet)
        #floor material
        self.floor_val=IntVar()
        self.rdt8=Radiobutton(self.search_w,text='None',variable=self.floor_val,value=1,command=self.floor)
        self.rdt9=Radiobutton(self.search_w,text='Ceramic',variable=self.floor_val,value=2,command=self.floor)
        self.rdt10=Radiobutton(self.search_w,text='Parquet',variable=self.floor_val,value=3,command=self.floor)
        self.rdt11=Radiobutton(self.search_w,text='Mosaic',variable=self.floor_val,value=4,command=self.floor)
        # other option
        self.option_val_bass=IntVar()
        self.option_val_garage=IntVar()
        self.option_val_elevator=IntVar()
        self.rdt12=Checkbutton(self.search_w,text='Basement',variable=self.option_val_bass,onvalue=1,offvalue=0,command=self.option)
        self.rdt13=Checkbutton(self.search_w,text='Garage',variable=self.option_val_garage,onvalue=1,offvalue=0,command=self.option)
        self.rdt14=Checkbutton(self.search_w,text='Elevator',variable=self.option_val_elevator,onvalue=1,offvalue=0,command=self.option)
  
        
        
        self.rdt4.grid(row=11,column=0)
        self.rdt5.grid(row=11,column=1)
        self.rdt6.grid(row=11,column=2)
        self.rdt7.grid(row=11,column=3)
        self.rdt8.grid(row=13,column=0)
        self.rdt9.grid(row=13,column=1)
        self.rdt10.grid(row=13,column=2)
        self.rdt11.grid(row=13,column=3)
        self.rdt12.grid(row=15,column=0)
        self.rdt13.grid(row=15,column=1)
        self.rdt14.grid(row=15,column=2)



        # addres drop down
        self.zone=StringVar()
        self.zone_val=[i for i in range(1,23)]
        self.zone.set('zone')
        self.drp_zn=ttk.Combobox(self.search_w,values=self.zone_val,textvariable=self.zone,width=9)
        self.drp_zn.grid(row=7,column=1,sticky='w',columnspan=2)
        self.drp_zn.bind("<<ComboboxSelected>>",self.loc_zone_add)    

        self.district=StringVar()
        self.district.set('district')  
        self.drp_ds=ttk.Combobox(self.search_w,textvariable=self.district,state='disable',width=9)
        self.drp_ds.grid(row=7,column=3,sticky='e',columnspan=2)


        # year

        self.pr_year_min=StringVar()
        self.pr_year_min.set('min')
        self.pr_val=[i for i in range(1340,1404)]
        self.drp_pr=ttk.Combobox(self.search_w,values=self.pr_val,textvariable=self.pr_year_min,width=9)
        self.drp_pr.grid(row=8,column=1)


        self.pr_year_max=StringVar()
        self.pr_year_max.set('max')
        self.pr_val=[i for i in range(1340,1404)]
        self.drp_pr=ttk.Combobox(self.search_w,values=self.pr_val,textvariable=self.pr_year_max,width=9)
        self.drp_pr.grid(row=8,column=3)



        self.btn=Button(self.search_w,text='search',border=3,relief='solid',width=40,command=self.search)
        self.btn.grid(row=16,column=0,columnspan=4)

    def search(self):

        self.find=Toplevel(self)
        self.find.title('find file')
        self.find.geometry('800x400+900+250')        

        self.txt=Text(self.find,border=3,relief='solid',state='disabled')
        self.txt.pack(expand=True,fill='both')

        try:
            search_sentence='SELECT * FROM house_for_sale WHERE '
            # type
            if self.rdt_val.get()==2:
                search_sentence+='Type="buy"'
            elif self.rdt_val.get()==1:
                search_sentence+='Type="rent"'

            
            # area
            if self.rdt_val.get()==2 or self.rdt_val.get()==1:   
                if len(self.entr1.get())>0 and len(self.entr2.get())>0:
                    search_sentence+=f' and Area>={int(self.entr1.get())} and Area<={int(self.entr2.get())}'

                elif len(self.entr1.get())>0 and len(self.entr2.get())==0:
                    search_sentence+=f' and Area>={int(self.entr1.get())} and Area<=10000000'
                    
                elif len(self.entr2.get())>0 and len(self.entr1.get())==0:
                    search_sentence+=f' and Area>=1 and Area<={int(self.entr2.get())}'

            else:
                if len(self.entr1.get())>0 and len(self.entr2.get())>0:
                    search_sentence+=f'Area>={int(self.entr1.get())} and Area<={int(self.entr2.get())}'

                elif len(self.entr1.get())>0 and len(self.entr2.get())==0:
                    search_sentence+=f'Area>={int(self.entr1.get())} and Area<=10000000'
                    
                elif len(self.entr2.get())>0 and len(self.entr1.get())==0:
                    search_sentence+=f'Area>=1 and Area<={int(self.entr2.get())}'
            
            # num of rooms
                    
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0:
                if len(self.entr3.get())>0 and len(self.entr4.get())>0:
                    search_sentence+=f' and Num_of_rooms>={int(self.entr3.get())} and Num_of_rooms<={int(self.entr4.get())}'
                elif len(self.entr3.get())>0 and len(self.entr4.get())==0:
                    search_sentence+=f' and Num_of_rooms>={int(self.entr3.get())} and Num_of_rooms<=1000000000'
                elif len(self.entr3.get())==0 and len(self.entr4.get())>0:
                    search_sentence+=f' and Num_of_rooms>=1 and Num_of_rooms<={int(self.entr4.get())}'
    
            else:
                if len(self.entr3.get())>0 and len(self.entr4.get())>0:
                    search_sentence+=f'Num_of_rooms>={int(self.entr3.get())} and Num_of_rooms<={int(self.entr4.get())}'
                elif len(self.entr3.get())>0 and len(self.entr4.get())==0:
                    search_sentence+=f'Num_of_rooms>={int(self.entr3.get())} and Num_of_rooms<=1000000000'
                elif len(self.entr3.get())==0 and len(self.entr4.get())>0:
                    search_sentence+=f'Num_of_rooms>=1 and Num_of_rooms<={int(self.entr4.get())}'
    
            # price per meter
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0:
                if len(self.entr5.get())>0 and len(self.entr6.get())>0:
                    search_sentence+=f' and Price_per_meter>={int(self.entr5.get())} and Price_per_meter<={int(self.entr6.get())}'
                elif len(self.entr5.get())>0 and len(self.entr6.get())==0:
                    search_sentence+=f' and Price_per_meter>={int(self.entr5.get())} and Price_per_meter<=1000000000'
                elif len(self.entr5.get())==0 and len(self.entr6.get())>0:
                    search_sentence+=f' and Price_per_meter>=1 and Price_per_meter<={int(self.entr6.get())}'
    
            else:
                if len(self.entr5.get())>0 and len(self.entr6.get())>0:
                    search_sentence+=f'Price_per_meter>={int(self.entr5.get())} and Price_per_meter<={int(self.entr6.get())}'
                elif len(self.entr5.get())>0 and len(self.entr6.get())==0:
                    search_sentence+=f'Price_per_meter>={int(self.entr5.get())} and Price_per_meter<=1000000000'
                elif len(self.entr5.get())==0 and len(self.entr6.get())>0:
                    search_sentence+=f'Price_per_meter>=1 and Price_per_meter<={int(self.entr6.get())}'
    
            # total price

            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0:
                if len(self.entr7.get())>0 and len(self.entr8.get())>0:
                    search_sentence+=f' and Total_price>={int(self.entr7.get())} and Total_price<={int(self.entr8.get())}'
                elif len(self.entr7.get())>0 and len(self.entr8.get())==0:
                    search_sentence+=f' and Total_price>={int(self.entr7.get())} and Total_price<=1000000000'
                elif len(self.entr7.get())==0 and len(self.entr8.get())>0:
                    search_sentence+=f' and Total_price>=1 and Total_price<={int(self.entr8.get())}'
    
            else:
                if len(self.entr7.get())>0 and len(self.entr8.get())>0:
                    search_sentence+=f'Total_price>={int(self.entr7.get())} and Total_price<={int(self.entr8.get())}'
                elif len(self.entr7.get())>0 and len(self.entr8.get())==0:
                    search_sentence+=f'Total_price>={int(self.entr7.get())} and Total_price<=1000000000'
                elif len(self.entr7.get())==0 and len(self.entr8.get())>0:
                    search_sentence+=f'Total_price>=1 and Total_price<={int(self.entr8.get())}'
            
            # deposit

            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0:
                if len(self.entr9.get())>0 and len(self.entr10.get())>0:
                    search_sentence+=f' and Deposit>={int(self.entr9.get())} and Deposit<={int(self.entr10.get())}'
                elif len(self.entr9.get())>0 and len(self.entr10.get())==0:
                    search_sentence+=f' and Deposit>={int(self.entr9.get())} and Deposit<=1000000000'
                elif len(self.entr9.get())==0 and len(self.entr10.get())>0:
                    search_sentence+=f' and Deposit>=1 and Deposit<={int(self.entr10.get())}'
    
            else:
                if len(self.entr9.get())>0 and len(self.entr10.get())>0:
                    search_sentence+=f'Deposit>={int(self.entr9.get())} and Deposit<={int(self.entr10.get())}'
                elif len(self.entr9.get())>0 and len(self.entr10.get())==0:
                    search_sentence+=f'Deposit>={int(self.entr9.get())} and Deposit<=1000000000'
                elif len(self.entr9.get())==0 and len(self.entr10.get())>0:
                    search_sentence+=f'Deposit>=1 and Deposit<={int(self.entr10.get())}'
            
            # monthly rents
                    
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 :
                if len(self.entr11.get())>0 and len(self.entr12.get())>0:
                    search_sentence+=f' and Monthly_rents>={int(self.entr11.get())} and Monthly_rents<={int(self.entr12.get())}'
                elif len(self.entr11.get())>0 and len(self.entr12.get())==0:
                    search_sentence+=f' and Monthly_rents>={int(self.entr11.get())} and Monthly_rents<=1200000000'
                elif len(self.entr11.get())==0 and len(self.entr12.get())>0:
                    search_sentence+=f' and Monthly_rents>=1 and Monthly_rents<={int(self.entr12.get())}'
    
            else:
                if len(self.entr11.get())>0 and len(self.entr12.get())>0:
                    search_sentence+=f'Monthly_rents>={int(self.entr11.get())} and Monthly_rents<={int(self.entr12.get())}'
                elif len(self.entr11.get())>0 and len(self.entr12.get())==0:
                    search_sentence+=f'Monthly_rents>={int(self.entr11.get())} and Monthly_rents<=1200000000'
                elif len(self.entr11.get())==0 and len(self.entr12.get())>0:
                    search_sentence+=f'Monthly_rents>=1 and Monthly_rents<={int(self.entr12.get())}'

            # floor

            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0:
                if len(self.entr13.get())>0 :
                    search_sentence+=f' and Floor={int(self.entr13.get())}'
            else:
                if len(self.entr13.get())>0 :
                    search_sentence+=f'Floor={int(self.entr13.get())}'

            # unit

            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0:
                if len(self.entr14.get())>0 :
                    search_sentence+=f' and Unit={int(self.entr14.get())}'
            else:
                if len(self.entr14.get())>0 :
                    search_sentence+=f'Unit={int(self.entr14.get())}'

            # zone
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0:
                if len(self.zone.get()) >0 and self.zone.get()!='zone' :
                    search_sentence+=f' and zone={int(self.zone.get())}'
            else:
                if len(self.zone.get()) >0 and self.zone.get()!='zone' :
                    search_sentence+=f'zone={int(self.zone.get())}'

            # district
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0   or self.zone.get()!='zone':
                if len(self.district.get()) >0 and self.district.get()!='district' :
                    search_sentence+=f' and district="{self.district.get()}"'
            else:
                if len(self.district.get()) >0 and self.district.get()!='district' :
                    search_sentence+=f'district="{self.district.get()}"'

            # year 
            
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0  or self.zone.get()!='zone':
                if self.pr_year_min.get()!='min' and self.pr_year_max.get()!='max':
                    search_sentence+=f' and Product_year>={int(self.pr_year_min.get())} and Product_year<={int(self.pr_year_max.get())}'
                elif self.pr_year_min.get()!='min' and self.pr_year_max.get()=='max':
                    search_sentence+=f' and Product_year>={int(self.pr_year_min.get())} and Product_year<=1000000000'
                elif self.pr_year_min.get()=='min'and self.pr_year_max.get()!='max':
                    search_sentence+=f' and Product_year>=1 and Product_year<={int(self.pr_year_max.get())}'
            else:
                if self.pr_year_min.get()!='min' and self.pr_year_max.get()!='max':
                    search_sentence+=f'Product_year>={int(self.pr_year_min.get())} and Product_year<={int(self.pr_year_max.get())}'
                elif self.pr_year_min.get()!='min' and self.pr_year_max.get()=='max':
                    search_sentence+=f'Product_year>={int(self.pr_year_min.get())} and Product_year<=1000000000'
                elif self.pr_year_min.get()=='min'and self.pr_year_max.get()!='max':
                    search_sentence+=f'Product_year>=1 and Product_year<={int(self.pr_year_max.get())}'
    
            # cabinet
        
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0 or self.pr_year_min.get()!='min' or self.pr_year_max.get()!='max':
                if self.cabinet_val.get()==1 :
                    search_sentence+=' and Cabinet_type="None"'
                if self.cabinet_val.get()==2 :
                    search_sentence+=' and Cabinet_type="MDF"'
                if self.cabinet_val.get()==3 :
                    search_sentence+=' and Cabinet_type="Chipboard"'
                if self.cabinet_val.get()==4 :
                    search_sentence+=' and Cabinet_type="High glass"'

            else:
                if self.cabinet_val.get()==1 :
                    search_sentence+=' Cabinet_type="None"'
                if self.cabinet_val.get()==2 :
                    search_sentence+=' Cabinet_type="MDF"'
                if self.cabinet_val.get()==3 :
                    search_sentence+=' Cabinet_type="Chipboard"'
                if self.cabinet_val.get()==4 :
                    search_sentence+=' Cabinet_type="High glass"'

            # floor self.floor_val

            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0 or self.pr_year_min.get()!='min' or self.pr_year_max.get()!='max' or self.cabinet_val.get()!=0 :
                if self.floor_val.get()==1 :
                    search_sentence+=' and Floor_material="None"'
                if self.floor_val.get()==2 :
                    search_sentence+=' and Floor_material="Ceramic"'
                if self.floor_val.get()==3 :
                    search_sentence+=' and Floor_material="Parquet"'
                if self.floor_val.get()==4 :
                    search_sentence+=' and Floor_material="Mosaic"'

            else:
                if self.floor_val.get()==1 :
                    search_sentence+=' Floor_material="None"'
                if self.floor_val.get()==2 :
                    search_sentence+=' Floor_material="Ceramic"'
                if self.floor_val.get()==3 :
                    search_sentence+=' Floor_material="Parquet"'
                if self.floor_val.get()==4 :
                    search_sentence+=' Floor_material="Mosaic"'

            # other option         self.option_val_bass self.option_val_garage self.option_val_elevator
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0 or self.pr_year_min.get()!='min' or self.pr_year_max.get()!='max' or self.cabinet_val.get()!=0 or self.floor_val.get()!=0 or self.option_val_garage.get()==1 or self.option_val_elevator.get()==1:
                if self.option_val_bass.get()==1 :
                    search_sentence+=' and option_basement="Basement"'
            else:
                if self.option_val_bass.get()==1 :
                    search_sentence+='option_basement="Basement"'
                
                
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0 or self.pr_year_min.get()!='min' or self.pr_year_max.get()!='max' or self.cabinet_val.get()!=0 or self.floor_val.get()!=0 or self.option_val_bass.get()==1 or self.option_val_elevator.get()==1:
                if self.option_val_garage.get()==1 :
                    search_sentence+=' and option_garage="Garage"'
            else:
                if self.option_val_garage.get()==1 :
                    search_sentence+='option_garage="Garage"'            
                
            if self.rdt_val.get()==2 or self.rdt_val.get()==1 or len(self.entr1.get())>0 or len(self.entr2.get())>0 or len(self.entr3.get())>0 or len(self.entr4.get())>0 or len(self.entr5.get())>0 or len(self.entr6.get())>0 or len(self.entr7.get())>0 or len(self.entr8.get())>0 or len(self.entr9.get())>0 or len(self.entr10.get())>0 or len(self.entr11.get())>0 and len(self.entr12.get())>0 or len(self.entr13.get())>0 or len(self.entr14.get())>0 or self.pr_year_min.get()!='min' or self.pr_year_max.get()!='max' or self.cabinet_val.get()!=0 or self.floor_val.get()!=0 or self.option_val_bass.get()==1 or self.option_val_garage.get()==1:
                if self.option_val_elevator.get()==1 :
                    search_sentence+=' and option_elevator="Elevator"'
            else:
                if self.option_val_elevator.get()==1 :
                    search_sentence+='option_elevator="Elevator"'



            self.my_cursor.execute(f'{search_sentence}')
            re=self.my_cursor.fetchall()
            for i in re:
                self.txt.config(state='normal')
                self.txt.insert(END,i)
                self.txt.insert(END,'\n')
        
        
        except:
            print('pleas enter one of search options')       

    def dark_theme(self):
        self.config(bg='#242221')

    def dark_theme_add(self):

        self.config(bg='#242221')
        self.add_w.config(bg='#242221')
        self.entr3.config(state='normal')
        self.entr5.config(state='normal')
        self.entr6.config(state='normal')
        self.lbl1.config(bg='#242221',fg='white')
        self.lbl2.config(bg='#242221',fg='white')
        self.lbl3.config(bg='#242221',fg='white')
        self.lbl4.config(bg='#242221',fg='white')
        self.lbl5.config(bg='#242221',fg='white')
        self.lbl6.config(bg='#242221',fg='white')
        self.lbl7.config(bg='#242221',fg='white')
        self.lbl8.config(bg='#242221',fg='white')
        self.lbl9.config(bg='#242221',fg='white')
        self.lbl10.config(bg='#242221',fg='white')
        self.lbl11.config(bg='#242221',fg='white')
        self.lbl12.config(bg='#242221',fg='white')
        self.lbl13.config(bg='#242221',fg='white')
        self.lbl14.config(bg='#242221',fg='white')
        self.lbl15.config(bg='#242221',fg='white')
        self.entr1.config(bg='#242221',fg='white')
        self.entr2.config(disabledbackground='#242221',bg='#242221',fg='white')
        self.entr3.config(disabledbackground='#242221',bg='#242221',fg='white')
        self.entr4.config(bg='#242221',fg='white')
        self.entr5.config(disabledbackground='#242221',bg='#242221',fg='white')
        self.entr6.config(disabledbackground='#242221',bg='#242221',fg='white')
        self.entr7.config(bg='#242221',fg='white')
        self.entr8.config(bg='#242221',fg='white')
        self.entr9.config(bg='#242221',fg='white')
        self.rdt1.config(bg='#242221',fg='white')
        self.rdt2.config(bg='#242221',fg='white')
        self.rdt4.config(bg='#242221',fg='white')
        self.rdt5.config(bg='#242221',fg='white')
        self.rdt6.config(bg='#242221',fg='white')
        self.rdt7.config(bg='#242221',fg='white')
        self.rdt8.config(bg='#242221',fg='white')
        self.rdt9.config(bg='#242221',fg='white')
        self.rdt10.config(bg='#242221',fg='white')
        self.rdt11.config(bg='#242221',fg='white')
        self.rdt12.config(bg='#242221',fg='white')
        self.rdt13.config(bg='#242221',fg='white')
        self.rdt14.config(bg='#242221',fg='white')
        self.entr3.config(state='disable')
        self.entr5.config(state='disable')
        self.entr6.config(state='disable')

    def dark_theme_search(self):
        self.config(bg='#242221')
        self.search_w.config(bg='#242221')
        self.lbl1.config(bg='#242221',fg='white')
        self.lbl2.config(bg='#242221',fg='white')
        self.lbl3.config(bg='#242221',fg='white')
        self.lbl4.config(bg='#242221',fg='white')
        self.lbl5.config(bg='#242221',fg='white')
        self.lbl6.config(bg='#242221',fg='white')
        self.lbl7.config(bg='#242221',fg='white')
        self.lbl8.config(bg='#242221',fg='white')
        self.lbl9.config(bg='#242221',fg='white')
        self.lbl10.config(bg='#242221',fg='white')
        self.lbl11.config(bg='#242221',fg='white')
        self.lbl12.config(bg='#242221',fg='white')
        self.lbl13.config(bg='#242221',fg='white')
        self.lbl14.config(bg='#242221',fg='white')
        self.entr1.config(bg='#242221',fg='white')
        self.entr2.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr3.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr4.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr5.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr6.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr7.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr8.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr9.config(bg='#242221',fg='white',disabledbackground='#242221')  
        self.entr10.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr11.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr12.config(bg='#242221',fg='white',disabledbackground='#242221')
        self.entr13.config(bg='#242221',fg='white')
        self.entr14.config(bg='#242221',fg='white')  
        self.rdt1.config(bg='#242221',fg='white')
        self.rdt2.config(bg='#242221',fg='white')
        self.rdt4.config(bg='#242221',fg='white')
        self.rdt5.config(bg='#242221',fg='white')
        self.rdt6.config(bg='#242221',fg='white')
        self.rdt7.config(bg='#242221',fg='white')
        self.rdt8.config(bg='#242221',fg='white')
        self.rdt9.config(bg='#242221',fg='white')
        self.rdt10.config(bg='#242221',fg='white')
        self.rdt11.config(bg='#242221',fg='white')
        self.rdt12.config(bg='#242221',fg='white')
        self.rdt13.config(bg='#242221',fg='white')
        self.rdt14.config(bg='#242221',fg='white')
        self.btn.config(bg='#242221',fg='black')

    def dark_theme_up(self):
        self.config(bg='#242221')
        self.delete_w.config(bg='#242221')
        self.lbl1.config(bg='#242221',fg='white')
        self.lbl2.config(bg='#242221',fg='white')
        self.lbl3.config(bg='#242221',fg='white')
        self.lbl4.config(bg='#242221',fg='white')
        self.lbl5.config(bg='#242221',fg='white')
        self.lbl6.config(bg='#242221',fg='white')
        self.lbl7.config(bg='#242221',fg='white')
        self.lbl8.config(bg='#242221',fg='white')
        self.lbl9.config(bg='#242221',fg='white')
        self.lbl10.config(bg='#242221',fg='white')
        self.lbl11.config(bg='#242221',fg='white')
        self.lbl12.config(bg='#242221',fg='white')
        self.lbl13.config(bg='#242221',fg='white')
        self.lbl14.config(bg='#242221',fg='white')
        self.lbl15.config(bg='#242221',fg='white')
        self.lbl16.config(bg='#242221',fg='white')
        self.entr1.config(bg='#242221',fg='white')
        self.entr2.config(bg='#242221',fg='white')
        self.entr3.config(bg='#242221',fg='white')
        self.entr4.config(bg='#242221',fg='white')
        self.entr5.config(bg='#242221',fg='white')
        self.entr6.config(bg='#242221',fg='white')
        self.entr7.config(bg='#242221',fg='white')
        self.entr8.config(bg='#242221',fg='white')
        self.entr9.config(bg='#242221',fg='white')  
        self.entr10.config(bg='#242221',fg='white')
        self.rdt1.config(bg='#242221',fg='white')
        self.rdt2.config(bg='#242221',fg='white')
        self.rdt4.config(bg='#242221',fg='white')
        self.rdt5.config(bg='#242221',fg='white')
        self.rdt6.config(bg='#242221',fg='white')
        self.rdt7.config(bg='#242221',fg='white')
        self.rdt8.config(bg='#242221',fg='white')
        self.rdt9.config(bg='#242221',fg='white')
        self.rdt10.config(bg='#242221',fg='white')
        self.rdt11.config(bg='#242221',fg='white')
        self.rdt12.config(bg='#242221',fg='white')
        self.rdt13.config(bg='#242221',fg='white')
        self.rdt14.config(bg='#242221',fg='white')
        self.rdt_delete.config(bg='#242221',fg='white')
        self.rdt_update.config(bg='#242221',fg='white')

    def light_theme(self):
        self.config(bg='white')

    def light_theme_add(self):

        self.config(bg='white')
        self.add_w.config(bg='white')
        self.lbl1.config(bg='white',fg='black')
        self.lbl2.config(bg='white',fg='black')
        self.lbl3.config(bg='white',fg='black')
        self.lbl4.config(bg='white',fg='black')
        self.lbl5.config(bg='white',fg='black')
        self.lbl6.config(bg='white',fg='black')
        self.lbl7.config(bg='white',fg='black')
        self.lbl8.config(bg='white',fg='black')
        self.lbl9.config(bg='white',fg='black')
        self.lbl10.config(bg='white',fg='black')
        self.lbl11.config(bg='white',fg='black')
        self.lbl12.config(bg='white',fg='black')
        self.lbl13.config(bg='white',fg='black')
        self.lbl14.config(bg='white',fg='black')
        self.lbl15.config(bg='white',fg='black')
        self.entr1.config(bg='white',fg='black')
        self.entr2.config(disabledbackground='white',bg='white',fg='black')
        self.entr3.config(disabledbackground='white',bg='white',fg='black')
        self.entr4.config(bg='white',fg='black')
        self.entr5.config(disabledbackground='white',bg='white',fg='black')
        self.entr6.config(disabledbackground='white',bg='white',fg='black')
        self.entr7.config(bg='white',fg='black')
        self.entr8.config(bg='white',fg='black')
        self.entr9.config(bg='white',fg='black')
        self.rdt1.config(bg='white',fg='black')
        self.rdt2.config(bg='white',fg='black')
        self.rdt4.config(bg='white',fg='black')
        self.rdt5.config(bg='white',fg='black')
        self.rdt6.config(bg='white',fg='black')
        self.rdt7.config(bg='white',fg='black')
        self.rdt8.config(bg='white',fg='black')
        self.rdt9.config(bg='white',fg='black')
        self.rdt10.config(bg='white',fg='black')
        self.rdt11.config(bg='white',fg='black')
        self.rdt12.config(bg='white',fg='black')
        self.rdt13.config(bg='white',fg='black')
        self.rdt14.config(bg='white',fg='black')

    def light_theme_search(self):
        self.config(bg='white')
        self.search_w.config(bg='white')
        self.lbl1.config(bg='white',fg='black')
        self.lbl2.config(bg='white',fg='black')
        self.lbl3.config(bg='white',fg='black')
        self.lbl4.config(bg='white',fg='black')
        self.lbl5.config(bg='white',fg='black')
        self.lbl6.config(bg='white',fg='black')
        self.lbl7.config(bg='white',fg='black')
        self.lbl8.config(bg='white',fg='black')
        self.lbl9.config(bg='white',fg='black')
        self.lbl10.config(bg='white',fg='black')
        self.lbl11.config(bg='white',fg='black')
        self.lbl12.config(bg='white',fg='black')
        self.lbl13.config(bg='white',fg='black')
        self.lbl14.config(bg='white',fg='black')
        self.entr1.config(bg='white',fg='black')
        self.entr2.config(disabledbackground='white',bg='white',fg='black')
        self.entr3.config(disabledbackground='white',bg='white',fg='black')
        self.entr4.config(disabledbackground='white',bg='white',fg='black')
        self.entr5.config(disabledbackground='white',bg='white',fg='black')
        self.entr6.config(disabledbackground='white',bg='white',fg='black')
        self.entr7.config(disabledbackground='white',bg='white',fg='black')
        self.entr8.config(disabledbackground='white',bg='white',fg='black')
        self.entr9.config(disabledbackground='white',bg='white',fg='black')  
        self.entr10.config(disabledbackground='white',bg='white',fg='black')
        self.entr11.config(disabledbackground='white',bg='white',fg='black')
        self.entr12.config(disabledbackground='white',bg='white',fg='black')
        self.entr13.config(bg='white',fg='black')
        self.entr14.config(bg='white',fg='black')  
        self.rdt1.config(bg='white',fg='black')
        self.rdt2.config(bg='white',fg='black')
        self.rdt4.config(bg='white',fg='black')
        self.rdt5.config(bg='white',fg='black')
        self.rdt6.config(bg='white',fg='black')
        self.rdt7.config(bg='white',fg='black')
        self.rdt8.config(bg='white',fg='black')
        self.rdt9.config(bg='white',fg='black')
        self.rdt10.config(bg='white',fg='black')
        self.rdt11.config(bg='white',fg='black')
        self.rdt12.config(bg='white',fg='black')
        self.rdt13.config(bg='white',fg='black')
        self.rdt14.config(bg='white',fg='black')
        self.btn.config(bg='white',fg='black')

    def light_theme_up(self):
        self.config(bg='white')
        self.delete_w.config(bg='white')
        self.lbl1.config(bg='white',fg='black')
        self.lbl2.config(bg='white',fg='black')
        self.lbl3.config(bg='white',fg='black')
        self.lbl4.config(bg='white',fg='black')
        self.lbl5.config(bg='white',fg='black')
        self.lbl6.config(bg='white',fg='black')
        self.lbl7.config(bg='white',fg='black')
        self.lbl8.config(bg='white',fg='black')
        self.lbl9.config(bg='white',fg='black')
        self.lbl10.config(bg='white',fg='black')
        self.lbl11.config(bg='white',fg='black')
        self.lbl12.config(bg='white',fg='black')
        self.lbl13.config(bg='white',fg='black')
        self.lbl14.config(bg='white',fg='black')
        self.lbl15.config(bg='white',fg='black')
        self.lbl16.config(bg='white',fg='black')
        self.entr1.config(bg='white',fg='black')
        self.entr2.config(bg='white',fg='black')
        self.entr3.config(bg='white',fg='black')
        self.entr4.config(bg='white',fg='black')
        self.entr5.config(bg='white',fg='black')
        self.entr6.config(bg='white',fg='black')
        self.entr7.config(bg='white',fg='black')
        self.entr8.config(bg='white',fg='black')
        self.entr9.config(bg='white',fg='black')  
        self.entr10.config(bg='white',fg='black')
        self.rdt1.config(bg='white',fg='black')
        self.rdt2.config(bg='white',fg='black')
        self.rdt4.config(bg='white',fg='black')
        self.rdt5.config(bg='white',fg='black')
        self.rdt6.config(bg='white',fg='black')
        self.rdt7.config(bg='white',fg='black')
        self.rdt8.config(bg='white',fg='black')
        self.rdt9.config(bg='white',fg='black')
        self.rdt10.config(bg='white',fg='black')
        self.rdt11.config(bg='white',fg='black')
        self.rdt12.config(bg='white',fg='black')
        self.rdt13.config(bg='white',fg='black')
        self.rdt14.config(bg='white',fg='black')
        self.rdt_delete.config(bg='white',fg='black')
        self.rdt_update.config(bg='white',fg='black')

    def update_file(self):

        if len (self.entr1.get(1.0,END))>1:
            if len(self.entr2.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Area={self.entr2.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')

            if len(self.entr3.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Num_of_rooms={self.entr3.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')
            
            if len(self.entr4.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Price_per_meter={self.entr4.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')            
            
            if len(self.entr5.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Total_price={self.entr5.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')
           
            if len(self.entr6.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Deposit={self.entr6.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')
           
            if len(self.entr7.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Monthly_rents={self.entr7.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')

            if len(self.entr8.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Full_addres="{self.entr8.get(1.0,END)}" WHERE rowid={self.entr1.get(1.0,END)}')

            if len(self.entr9.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Floor={self.entr9.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')

            if len(self.entr10.get(1.0,END))>1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Unit={self.entr10.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')
            
            if self.rdt_val.get()==2:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Type="buy",Deposit=" ",Monthly_rents=" ",Price_per_meter={self.entr4.get(1.0,END)},Total_price={self.entr5.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')           
            if self.rdt_val.get()==1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Type="rent",Price_per_meter=" ",Total_price=" ",Deposit={self.entr9.get(1.0,END)},Monthly_rents={self.entr9.get(1.0,END)} WHERE rowid={self.entr1.get(1.0,END)}')
            else:
                pass

            self.my_cursor.execute(f'UPDATE house_for_sale SET Zone={self.zone.get()} WHERE rowid={self.entr1.get(1.0,END)}')
            self.my_cursor.execute(f'UPDATE house_for_sale SET district="{self.district.get()}" WHERE rowid={self.entr1.get(1.0,END)}')
            self.my_cursor.execute(f'UPDATE house_for_sale SET Product_year={self.pr_year.get()} WHERE rowid={self.entr1.get(1.0,END)}')

            if self.cabinet_val.get()==1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Cabinet_type="None" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.cabinet_val.get()==2:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Cabinet_type="MDF" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.cabinet_val.get()==3:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Cabinet_type="Chipboard" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.cabinet_val.get()==4:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Cabinet_type="High glass" WHERE rowid={self.entr1.get(1.0,END)}')


            if self.floor_val.get()==1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Floor_material="None" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.floor_val.get()==2:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Floor_material="Ceramic" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.floor_val.get()==3:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Floor_material="Parquet" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.floor_val.get()==4:
                self.my_cursor.execute(f'UPDATE house_for_sale SET Floor_material="Mosaic" WHERE rowid={self.entr1.get(1.0,END)}')


            if self.option_val_bass.get()==1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET option_basement="Basement" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.option_val_bass.get()==0:
                self.my_cursor.execute(f'UPDATE house_for_sale SET option_basement="" WHERE rowid={self.entr1.get(1.0,END)}')


            if self.option_val_garage.get()==1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET option_garage="Garage" WHERE rowid={self.entr1.get(1.0,END)}')
            elif self.option_val_garage.get()==0:
                self.my_cursor.execute(f'UPDATE house_for_sale SET option_garage="" WHERE rowid={self.entr1.get(1.0,END)}')

            if self.option_val_elevator.get()==1:
                self.my_cursor.execute(f'UPDATE house_for_sale SET option_elevator="Elevator" WHERE rowid={self.entr1.get(1.0,END)}')
            if self.option_val_elevator.get()==0:
                self.my_cursor.execute(f'UPDATE house_for_sale SET option_elevator="" WHERE rowid={self.entr1.get(1.0,END)}')




        else:
            print('enter file code')

    def delete_file(self):
        self.entr1.config(state='normal')
        try:
            self.my_cursor.execute(f'DELETE FROM house_for_sale WHERE rowid={self.entr1.get(1.0,END)}')
            self.conector.commit()
        except:
            pass

    def search_file(self):


        try:
            self.rdt1.config(state='normal')
            self.rdt2.config(state='normal')
            self.rdt4.config(state='normal')
            self.rdt5.config(state='normal')
            self.rdt6.config(state='normal')
            self.rdt7.config(state='normal')
            self.rdt8.config(state='normal')
            self.rdt9.config(state='normal')
            self.rdt10.config(state='normal')
            self.rdt11.config(state='normal')
            self.rdt12.config(state='normal')
            self.rdt13.config(state='normal')
            self.rdt14.config(state='normal')
            self.entr1.config(state='normal')
            self.entr2.config(state='normal')
            self.entr3.config(state='normal')
            self.entr8.config(state='normal')
            self.entr9.config(state='normal')
            self.entr10.config(state='normal')
            self.drp_zn.config(state=('normal'))
            self.drp_ds.config(state=('normal'))
            self.drp_pr.config(state='normal')
            
            
            self.my_cursor.execute(f'SELECT * FROM house_for_sale WHERE rowid={self.entr1.get(1.0,END)}')
            se=self.my_cursor.fetchall()

            if se[0][0]=='buy':

                self.rdt_val.set(2)
                self.entr6.config(state='disabled')
                self.entr7.config(state='disabled')
                self.entr4.config(state='normal')
                self.entr5.config(state='normal')

            
            elif se[0][0]=='rent':

                self.rdt_val.set(1)
                self.entr4.config(state='disabled')
                self.entr5.config(state='disabled')
                self.entr6.config(state='normal')
                self.entr7.config(state='normal')

            self.entr2.insert(END,se[0][1])
            self.entr3.insert(END,se[0][2])
            self.entr4.insert(END,se[0][3])
            self.entr5.insert(END,se[0][4])
            self.entr6.insert(END,se[0][5])
            self.entr7.insert(END,se[0][6])
            self.entr8.insert(END,se[0][9])
            self.entr9.insert(END,se[0][10])
            self.entr10.insert(END,se[0][11])




            self.zone.set(se[0][7])
            self.district.set(se[0][8])
            self.pr_year.set(se[0][12])
            # cabinet
            if se[0][13]=="None":
                self.cabinet_val.set(1)

            elif se[0][13]=="MDF":
                self.cabinet_val.set(2)
            
            elif se[0][13]=="Chipboard":
                self.cabinet_val.set(3)
            
            elif se[0][13]=="High glass":
                self.cabinet_val.set(4)
            

            # floor
            if se[0][14]=="None":
                self.floor_val.set(1)
            elif se[0][14]=="Ceramic":
                self.floor_val.set(2)
            elif se[0][14]=="Parquat":
                self.floor_val.set(3)        
            elif se[0][14]=="Mosaic":
                self.floor_val.set(4)
            # option

            if se[0][15]=="Basement":
                self.option_val_bass.set(1)
            if se[0][16]=="Garage":
                self.option_val_garage.set(1)
            if se[0][17]=="Elevator":
                self.option_val_elevator.set(1)
        except:
            print('file code is empty')

    def update_delet_item(self):

        self.delete_w=Toplevel(self)
        self.delete_w.title('update / delete item')
        self.delete_w.geometry('1000x600+600+250')


        self.m=Menu(self.delete_w)
        self.menu=Menu(self.m,tearoff=0)
        self.menu.add_command(label='add item',command=self.add_item)
        self.menu.add_command(label='search item',command=self.search)
        self.menu.add_command(label='update/delete item',command=self.update_delet_item)
        self.menu.add_separator()
        self.menu.add_command(label='quit',command=lambda:self.destroy())
        self.m.add_cascade(label='actions',menu=self.menu)

        self.menu2=Menu(self.m)
        self.menu2.add_command(label='dark',command=self.dark_theme_up)
        self.menu2.add_command(label='light',command=self.light_theme_up)
        self.m.add_cascade(label='theme',menu=self.menu2)
        self.config(menu=self.m)


        self.lbl1=Label(self.delete_w,text='File Code:',font=('Times New Roman',20))
        self.lbl2=Label(self.delete_w,text='Type:',font=('Times New Roman',20))
        self.lbl3=Label(self.delete_w,text='Area:',font=('Times New Roman',20))
        self.lbl4=Label(self.delete_w,text='Num of rooms:',font=('Times New Roman',20))
        self.lbl5=Label(self.delete_w,text='Price per meter:',font=('Times New Roman',20))
        self.lbl6=Label(self.delete_w,text='Total price:',font=('Times New Roman',20))
        self.lbl7=Label(self.delete_w,text='Deposit:',font=('Times New Roman',20))
        self.lbl8=Label(self.delete_w,text='Monthly rents:',font=('Times New Roman',20))
        self.lbl9=Label(self.delete_w,text='Address:',font=('Times New Roman',20))
        self.lbl10=Label(self.delete_w,text='Full address:',font=('Times New Roman',20))
        self.lbl11=Label(self.delete_w,text='Floor:',font=('Times New Roman',20))
        self.lbl12=Label(self.delete_w,text='Unit:',font=('Times New Roman',20))
        self.lbl13=Label(self.delete_w,text='Product year:',font=('Times New Roman',20))
        self.lbl14=Label(self.delete_w,text='Cabinet type:',font=('Times New Roman',20))
        self.lbl15=Label(self.delete_w,text='Floor material:',font=('Times New Roman',20))
        self.lbl16=Label(self.delete_w,text='Other options:',font=('Times New Roman',20))
        

    
        self.lbl1.grid(row=1,column=0,sticky='w')
        self.lbl2.grid(row=2,column=0,sticky='w')
        self.lbl3.grid(row=3,column=0,sticky='w')
        self.lbl4.grid(row=4,column=0,sticky='w')
        self.lbl5.grid(row=5,column=0,sticky='w')
        self.lbl6.grid(row=6,column=0,sticky='w')
        self.lbl7.grid(row=7,column=0,sticky='w')
        self.lbl8.grid(row=8,column=0,sticky='w')
        self.lbl9.grid(row=9,column=0,sticky='w')
        self.lbl10.grid(row=10,column=0,sticky='w')
        self.lbl11.grid(row=11,column=0,sticky='w')
        self.lbl12.grid(row=11,column=2,sticky='w')
        self.lbl13.grid(row=11,column=4,sticky='w')
        self.lbl14.grid(row=12,column=0,sticky='w')
        self.lbl15.grid(row=14,column=0,sticky='w')
        self.lbl16.grid(row=16,column=0,sticky='w')


        self.entr1=Text(self.delete_w,width=100,height=1,border=3,relief='solid')
        self.entr2=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr3=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr4=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr5=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr6=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr7=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr8=Text(self.delete_w,width=100,height=1,border=3,relief='solid',state='disabled')
        self.entr9=Text(self.delete_w,border=3,width=28,height=1,relief='solid',state='disabled')
        self.entr10=Text(self.delete_w,border=3,width=28,height=1,relief='solid',state='disabled')

        self.entr1.grid(row=1,column=1,columnspan=5)
        self.entr2.grid(row=3,column=1,columnspan=5)
        self.entr3.grid(row=4,column=1,columnspan=5)
        self.entr4.grid(row=5,column=1,columnspan=5)
        self.entr5.grid(row=6,column=1,columnspan=5)
        self.entr6.grid(row=7,column=1,columnspan=5)
        self.entr7.grid(row=8,column=1,columnspan=5)
        self.entr8.grid(row=10,column=1,columnspan=5)
        self.entr9.grid(row=11,column=1)
        self.entr10.grid(row=11,column=3)

        # rent buy
        self.rdt_val=IntVar()
        self.rdt1=Radiobutton(self.delete_w,text='Rent',variable=self.rdt_val,value=1,command=self.rent_buy_delet_file,state='disabled')
        self.rdt2=Radiobutton(self.delete_w,text='Buy',variable=self.rdt_val,value=2,command=self.rent_buy_delet_file,state='disabled')
        # cabinet type
        self.cabinet_val=IntVar()
        self.rdt4=Radiobutton(self.delete_w,text='None',variable=self.cabinet_val,value=1,command=self.cabinet_delet,state='disabled')
        self.rdt5=Radiobutton(self.delete_w,text='MDF',variable=self.cabinet_val,value=2,command=self.cabinet_delet,state='disabled')
        self.rdt6=Radiobutton(self.delete_w,text='Chipboard',variable=self.cabinet_val,value=3,command=self.cabinet_delet,state='disabled')
        self.rdt7=Radiobutton(self.delete_w,text='High glass',variable=self.cabinet_val,value=4,command=self.cabinet_delet,state='disabled')
        #floor material
        self.floor_val=IntVar()
        self.rdt8=Radiobutton(self.delete_w,text='None',variable=self.floor_val,value=1,command=self.floor,state='disabled')
        self.rdt9=Radiobutton(self.delete_w,text='Ceramic',variable=self.floor_val,value=2,command=self.floor,state='disabled')
        self.rdt10=Radiobutton(self.delete_w,text='Parquet',variable=self.floor_val,value=3,command=self.floor,state='disabled')
        self.rdt11=Radiobutton(self.delete_w,text='Mosaic',variable=self.floor_val,value=4,command=self.floor,state='disabled')
        # other option
        self.option_val_bass=IntVar()
        self.option_val_garage=IntVar()
        self.option_val_elevator=IntVar()
        self.rdt12=Checkbutton(self.delete_w,text='Basement',variable=self.option_val_bass,onvalue=1,offvalue=0,command=self.option,state='disabled')
        self.rdt13=Checkbutton(self.delete_w,text='Garage',variable=self.option_val_garage,onvalue=1,offvalue=0,command=self.option,state='disabled')
        self.rdt14=Checkbutton(self.delete_w,text='Elevator',variable=self.option_val_elevator,onvalue=1,offvalue=0,command=self.option,state='disabled')


        self.rdt1.grid(row=2,column=2)
        self.rdt2.grid(row=2,column=3)
        self.rdt4.grid(row=13,column=0)
        self.rdt5.grid(row=13,column=1)
        self.rdt6.grid(row=13,column=2)
        self.rdt7.grid(row=13,column=3)
        self.rdt8.grid(row=15,column=0)
        self.rdt9.grid(row=15,column=1)
        self.rdt10.grid(row=15,column=2)
        self.rdt11.grid(row=15,column=3)
        self.rdt12.grid(row=17,column=0)
        self.rdt13.grid(row=17,column=1)
        self.rdt14.grid(row=17,column=2)

        self.btn1=Button(self.delete_w,text='Search',font=('Times New Roman',20),width=60,border=3,relief='solid',command=self.search_file)
        self.btn2=Button(self.delete_w,text='Update',font=('Times New Roman',20),width=20,border=3,relief='solid',command=self.update_file)
        self.btn3=Button(self.delete_w,text='Delete',font=('Times New Roman',20),width=20,border=3,relief='solid',command=self.delete_file)
        self.btn4=Button(self.delete_w,text='show files',font=('Times New Roman',20),width=20,border=3,relief='solid',command=self.show_file)


        self.btn1.grid(row=18,column=0,columnspan=6)
        self.btn2.grid(row=19,column=0,columnspan=2)
        self.btn3.grid(row=19,column=4,columnspan=2)
        self.btn4.grid(row=19,column=2,columnspan=2)        

        # addres drop down
        self.zone=StringVar()
        self.zone_val=[i for i in range(1,23)]
        self.zone.set('zone')
        self.drp_zn=ttk.Combobox(self.delete_w,values=self.zone_val,textvariable=self.zone,state='disabled')
        self.drp_zn.grid(row=9,column=1)
        self.drp_zn.bind("<<ComboboxSelected>>",self.loc_zone_add)    

        self.district=StringVar()
        self.district.set('district')  
        self.drp_ds=ttk.Combobox(self.delete_w,textvariable=self.district,state='disable')
        self.drp_ds.grid(row=9,column=3)


        # product year

        self.pr_year=IntVar()
        self.pr_year.set('year')
        self.pr_val=[i for i in range(1340,1404)]
        self.drp_pr=ttk.Combobox(self.delete_w,values=self.pr_val,textvariable=self.pr_year,state='disabled')
        self.drp_pr.grid(row=11,column=5)


        self.del_up_val=IntVar()
        self.rdt_delete=Radiobutton(self.delete_w,text='Delete',variable=self.del_up_val,value=1,command=self.del_up)
        self.rdt_update=Radiobutton(self.delete_w,text='Update',variable=self.del_up_val,value=2,command=self.del_up)

        self.rdt_delete.grid(row=0,column=2)
        self.rdt_update.grid(row=0,column=3)

    def del_up(self):
        if self.del_up_val.get()==1:
            self.entr1.config(state='normal')
            self.entr2.config(state='disabled')
            self.entr3.config(state='disabled')
            self.entr4.config(state='disabled')
            self.entr5.config(state='disabled')
            self.entr6.config(state='disabled')
            self.entr7.config(state='disabled')
            self.entr8.config(state='disabled')
            self.entr9.config(state='disabled')
            self.entr10.config(state='disabled')
        elif self.del_up_val.get()==2:
            self.entr1.config(state='normal')
            self.entr2.config(state='normal')
            self.entr3.config(state='normal')
            self.entr4.config(state='normal')
            self.entr5.config(state='normal')
            self.entr6.config(state='normal')
            self.entr7.config(state='normal')
            self.entr8.config(state='normal')
            self.entr9.config(state='normal')
            self.entr10.config(state='normal')
            self.rdt1.config(state='normal')
            self.rdt2.config(state='normal')
            self.rdt4.config(state='normal')
            self.rdt5.config(state='normal')
            self.rdt6.config(state='normal')
            self.rdt7.config(state='normal')
            self.rdt8.config(state='normal')
            self.rdt9.config(state='normal')
            self.rdt10.config(state='normal')
            self.rdt11.config(state='normal')
            self.rdt12.config(state='normal')
            self.rdt13.config(state='normal')
            self.rdt14.config(state='normal')
            self.drp_zn.config(state='normal')
            self.drp_pr.config(state='normal')



if __name__ == "__main__":
    main=Real_state()
    main.mainloop()
main.create_database()

