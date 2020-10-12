from tkinter import *
import math,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Bill Reciept")
        bg_color="#074463"
        t=Label(self.root,text="Billing Software",bd=12,fg="white",bg=bg_color,relief=GROOVE,font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #==========  variables =================#

         #==========  cosmetics =================#
        self.bath=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_shampoo=IntVar()
        self.hair_gel=IntVar()
        self.body_loashan=IntVar()

        #===============grocery===================#

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()


        #=================cold drinks================#

        self.maza=IntVar()
        self.cococola=IntVar()
        self.frooti=IntVar()
        self.thumbs_up=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #==============total cosmetic , grocery , drinks price and tax ===========================#

        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()


        #================== Customer =======================#

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set((x))
        self.search_bill=StringVar()


         # =============customer frame =======================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer details",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name :",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)


        cphn_label=Label(F1,text="Phone No.:",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font="arial 15",bd=7,textvariable=self.c_phon,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_label=Label(F1,text="Bill Number:",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font="arial 15",bd=7,textvariable=self.search_bill,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=5)

        #================= Cosmetic Frame ==========================#
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath soap",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.bath,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)


        face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5,sticky="w")
        face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        Hair_shampoo_lbl=Label(F2,text="Hair Shampoo",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=5,sticky="w")
        Hair_shampoo_txt=Entry(F2,width=10,textvariable=self.hair_shampoo,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        Hair_gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=5,sticky="w")
        Hair_gel_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl=Label(F2,text="Body Loshan",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=5,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.body_loashan,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================= Grocery Frame ==========================#
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        F3.place(x=335,y=180,width=275,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        food_oil_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5,sticky="w")
        food_oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)


        daal_lbl=Label(F3,text="Daal",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5,sticky="w")
        daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=5,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        sugar_lbl=Label(F3,text="sugar",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=5,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=5,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        
        #================= Cpld Drink Frame ==========================#
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        F4.place(x=620,y=180,width=275,height=380)

        Maza_lbl=Label(F4,text="Maza",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5,sticky="w")
        Maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        cococola_lbl=Label(F4,text="Cococola",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5,sticky="w")
        cococola_txt=Entry(F4,width=10,textvariable=self.cococola,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)


        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        thumbs_up_lbl=Label(F4,text="Thumbs up",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=5,sticky="w")
        thumbs_up_txt=Entry(F4,width=10,textvariable=self.thumbs_up,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        Limca_lbl=Label(F4,text="Limca",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=5,sticky="w")
        Limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=5,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #================= Bill Area Frame ==========================#
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=915,y=180,width=355,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #================= Button Frame ==========================#
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1=Label(F6,text="Total cosmetic price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Grocery price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Cold Drink price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)



        c1=Label(F6,text="cosmetic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Grocery Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Cold Drink Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=520,height=100)

        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",bd=2,pady=10,width=9,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        bill_btn=Button(btn_f,text="Genrate Bill",bg="cadetblue",command=self.bill_area,fg="white",bd=2,pady=10,width=9,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",bg="cadetblue",fg="white",bd=2,pady=10,width=9,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_f,text="Exit",bg="cadetblue",fg="white",bd=2,pady=10,width=9,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        #self.welcome_bill()

    def total(self):

        #===============get cosmetics value ========================#

        self.c_bs_p=self.bath.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.hair_shampoo.get()*180
        self.c_hg_p=self.hair_gel.get()*140
        self.c_bl_p=self.body_loashan.get()*180
        self.total_cosmetic_price=float(

                                    (self.c_bs_p)+
                                    (self.c_fc_p)+
                                    (self.c_fw_p)+
                                    (self.c_hs_p)+
                                    (self.c_hg_p)+
                                    (self.c_bl_p)
                                     )

        self.cosmetics_price.set(" Rs. " +str(self.total_cosmetic_price))
        self.cosmetics_tax.set(" Rs. " +str(round((self.total_cosmetic_price *0.05),2)))

                        #===============get grocery value ========================#

        self.c_r_p=self.rice.get()*80
        self.c_fo_p=self.food_oil.get()*180
        self.c_d_p=self.daal.get()*60
        self.c_w_p=self.wheat.get()*100
        self.c_s_p=self.sugar.get()*40
        self.c_t_p=self.tea.get()*120
        self.total_grocery_price=float(

                                    (self.c_r_p)+
                                    (self.c_fo_p)+
                                    (self.c_d_p)+
                                    (self.c_w_p)+
                                    (self.c_s_p)+
                                    (self.c_t_p)
                                     )

        self.grocery_price.set(" Rs. " +str(self.total_grocery_price))
        self.grocery_tax.set(" Rs. " +str(round((self.total_grocery_price *0.1),2)))


               #===============get cold drink value ========================#

        self.c_m_p=self.maza.get()*80
        self.c_co_p=self.cococola.get()*40
        self.c_f_p=self.frooti.get()*60
        self.c_tu_p=self.thumbs_up.get()*35
        self.c_l_p=self.limca.get()*38
        self.c_sp_p=self.sprite.get()*45

        self.total_cold_drink_price=float(

                                    (self.c_m_p)+
                                    (self.c_co_p)+
                                    (self.c_f_p)+
                                    (self.c_tu_p)+
                                    (self.c_l_p)+
                                    (self.c_sp_p)
                                        )

        self.cold_drink_price.set(" Rs. " + str(self.total_cold_drink_price))
        self.cold_drink_tax.set(" Rs. " +str(round((self.total_cold_drink_price *0.05),2)))



    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome to SAGGY Retail")
        self.textarea.insert(END,f"\n Bill Number:- { self.bill_no.get() } ")
        self.textarea.insert(END,f"\n Customer Name :- { self.c_name.get() }")
        self.textarea.insert(END,f"\n Phone Number :-  { self.c_phon.get() }")
        self.textarea.insert(END,f"\n ======================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tRs")
        self.textarea.insert(END,f"\n ======================================")

    def bill_area(self):
        self.welcome_bill()
        #======================cosmetic=======================#
        if self.bath.get() != 0:
            self.textarea.insert(END,f"\n Bath soap\t\t{self.bath.get()}\t\t{self.c_bs_p}")
        if self.face_cream.get() != 0:
            self.textarea.insert(END,f"\n Face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.face_wash.get() != 0:
            self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
        if self.hair_shampoo.get() != 0:
            self.textarea.insert(END,f"\n Hair Shampoo\t\t{self.hair_shampoo.get()}\t\t{self.c_hs_p}")
        if self.hair_gel.get() != 0:
           self.textarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_hg_p}")
        if self.body_loashan.get() != 0:
            self.textarea.insert(END,f"\n Body loshan\t\t{self.body_loashan.get()}\t\t{self.c_bl_p}")

        #======================grocery=======================#
        if self.rice.get() != 0:
            self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.c_r_p}")
        if self.food_oil.get() != 0:
            self.textarea.insert(END,f"\n Food oil\t\t{self.face_cream.get()}\t\t{self.c_fo_p}")
        if self.daal.get() != 0:
            self.textarea.insert(END,f"\n Daal\t\t{self.face_wash.get()}\t\t{self.c_d_p}")
        if self.wheat.get() != 0:
            self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.c_w_p}")
        if self.sugar.get() != 0:
           self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.c_s_p}")
        if self.tea.get() != 0:
            self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.c_t_p}")

        #======================cold drink=======================#
        if self.maza.get() != 0:
            self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.c_m_p}")
        if self.cococola.get() != 0:
            self.textarea.insert(END,f"\n Cococola\t\t{self.cococola.get()}\t\t{self.c_co_p}")
        if self.thumbs_up.get() != 0:
            self.textarea.insert(END,f"\n Thumbs up\t\t{self.thumbs_up.get()}\t\t{self.c_tu_p}")
        if self.frooti.get() != 0:
            self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.c_f_p}")
        if self.limca.get() != 0:
           self.textarea.insert(END,f"\n Limca\t\t{self.sugar.get()}\t\t{self.c_l_p}")
        if self.sprite.get() != 0:
            self.textarea.insert(END,f"\n Sprite\t\t{self.tea.get()}\t\t{self.c_sp_p}")

        else:
            pass





root=Tk()
obj=Bill_App(root)
root.mainloop()