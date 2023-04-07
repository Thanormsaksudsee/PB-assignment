records = {'HomePage':['Login','RecommentShop','flash sale','Profile member','Messenger','Help','SeachProduct','RecommentProduct','Cart'],
         
         'Login':["HomePage",'Register'],
         
         'Register':['Login',"HomePage"],
         
         'FollowProduct':["HomePage",'LastOreder'],
         
         'ReccommentShop':['Cart',"HomePage"],
         
         'flash sale':['Cart',"HomePage"],
         
         'Profile member':['Order','Logout',"Favorite","CancellationReturn","ManageProfile","HomePage"],
         
         "Messenger":["HomePage"],
         
         "Help":["HomePage",'FollowProduct'],
         
         'product coupons':["HomePage"],
         
         'SeachProduct':["HomePage",'ReccommentShop','RecommentProduct'],
         
         'RecommentProduct':["HomePage",'Cart','flash sale'],
         
         'Cart':["HomePage",'RecommentProduct',"SeachPRoduct","Messenger","Profile member",'product coupons']}

def Bigkuma():
    
    def Grahp():
        keep = 'y'
        while keep == 'y':
            print('1.วางโหนดตามวงกลม')
            print('2.วางโหนดโดยใช้แนวคิดของ "Force-directed placement algorithm')
            print('3.วางโหนดแบบสุ่ม')
            print('4.วางโหนดตามแนววงศ์')
            
            Select = int(input('Please Seclect Funtion : '))
            
            if Select == 1:
                Grahp1circular_layout()()
            elif Select == 2:
                Grahp2kamada_kawai_layout()
            elif Select == 3:
                Grahp3random_layout()
            elif Select == 4:
                Grahp4shell_layout()
            else:
                print('อย่าเปรี้ยวไอสัสพิมพ์ดีๆ')
                
            keep = input('Enter y for Moretime Enter n for Exit left Client: ').lower()
    def Grahp1circular_layout():#วางโหนดตามวงกลม
        import networkx as nx
        import matplotlib.pyplot as plt

        # สร้างกราฟ
        G = nx.DiGraph()

        # เพิ่ม vertex
        G.add_node('HomePage')
        G.add_node('Register')
        G.add_node('FollowProduct')
        G.add_node('ReccommentShop')
        G.add_node('flash sale')
        G.add_node('Profile member')
        G.add_node('Messenger')
        G.add_node('Help')
        G.add_node('product coupons')
        G.add_node('SeachProduct')
        G.add_node('RecommentProduct')
        G.add_node('LastOreder')
        G.add_node('Cart')
        G.add_node('Order')
        G.add_node('Favorite')
        G.add_node('CancellationReturn')
        G.add_node('ManageProfile')

        # เพิ่ม edge และระบุทิศทาง
        G.add_edge('HomePage', 'Login',)
        G.add_edge('HomePage', 'ReccommentShop',)
        G.add_edge('HomePage', 'flash sale',)
        G.add_edge('HomePage', 'Profile member',)
        G.add_edge('HomePage', 'Messenger',)
        G.add_edge('HomePage', 'Help',)
        G.add_edge('HomePage', 'SeachProduct',)
        G.add_edge('HomePage', 'RecommentProduct',)
        G.add_edge('HomePage', 'Cart',)

        G.add_edge('Login', 'HomePage',)
        G.add_edge('Login', 'Register',)

        G.add_edge('Register', 'Login',)
        G.add_edge('Register', 'HomePage',)

        G.add_edge('FollowProduct', 'LastOreder',)
        G.add_edge('FollowProduct', 'HomePage',)

        G.add_edge('ReccommentShop', 'Cart',)
        G.add_edge('ReccommentShop', 'HomePage',)

        G.add_edge('flash sale', 'Cart',)
        G.add_edge('flash sale', 'HomePage',)

        G.add_edge('Profile member', 'Order',)
        G.add_edge('Profile member', 'Logout',)
        G.add_edge('Profile member', 'Favorite',)
        G.add_edge('Profile member', 'CancellationReturn',)
        G.add_edge('Profile member', 'ManageProfile',)
        G.add_edge('Profile member', 'HomePage',)

        G.add_edge('Help', 'HomePage',)
        G.add_edge('Help', 'FollowProduct',)

        G.add_edge('Messenger', 'HomePage',)


        G.add_edge('product coupons', 'HomePage',)

        G.add_edge('SeachProduct', 'HomePage',)
        G.add_edge('SeachProduct', 'ReccommentShop',)
        G.add_edge('SeachProduct', 'RecommentProduct',)

        G.add_edge('RecommentProduct', 'HomePage',)
        G.add_edge('RecommentProduct', 'Cart',)
        G.add_edge('RecommentProduct', 'flash sale',)

        G.add_edge('Cart', 'HomePage',)
        G.add_edge('Cart', 'RecommentProduct',)
        G.add_edge('Cart', 'SeachPRoduct',)
        G.add_edge('Cart', 'Messenger',)
        G.add_edge('Cart', 'Profile member',)
        G.add_edge('Cart', 'product coupons',)


        # พล็อตกราฟและระบุทิศทางของ edge
        fig, ax = plt.subplots(figsize=(15, 12)) # กำหนดขนาดของกราฟ
        pos = nx.circular_layout(G)  # เปลี่ยน layout เป็น 'circular'
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos, font_size=10)  # เปลี่ยนขนาด font เป็น 12
        nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
        # ระบุจุดเริ่มและสิ้นสุด
        startPoint = str(input("Enter start point:"))
        endPoint = str(input("Enter end point:"))

        # ระบุจุดจากที่หนึ่งไปยังอีกที่ว่าผ่านจุดใดบ้าง
        path = nx.shortest_path(G, startPoint, endPoint)
        print(path)

        path = nx.shortest_path(G, source=startPoint, target=endPoint)

        # แสดงกราฟที่ระบุเส้นทางแล้ว
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, edge_color='gray')  # ให้สีเส้นเป็นสีเทา
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

        # เปลี่ยนสีของเส้นทางที่ผ่านไปทั้งหมดใน path เป็นสีแดง
        for i in range(len(path)-1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2.0)
        plt.show()
    def Grahp2kamada_kawai_layout():#วางโหนดโดยใช้แนวคิดของ "Force-directed placement algorithm
        import networkx as nx
        import matplotlib.pyplot as plt

        # สร้างกราฟ
        G = nx.DiGraph()

        # เพิ่ม vertex
        G.add_node('HomePage')
        G.add_node('Register')
        G.add_node('FollowProduct')
        G.add_node('ReccommentShop')
        G.add_node('flash sale')
        G.add_node('Profile member')
        G.add_node('Messenger')
        G.add_node('Help')
        G.add_node('product coupons')
        G.add_node('SeachProduct')
        G.add_node('RecommentProduct')
        G.add_node('LastOreder')
        G.add_node('Cart')
        G.add_node('Order')
        G.add_node('Favorite')
        G.add_node('CancellationReturn')
        G.add_node('ManageProfile')

        # เพิ่ม edge และระบุทิศทาง
        G.add_edge('HomePage', 'Login',)
        G.add_edge('HomePage', 'ReccommentShop',)
        G.add_edge('HomePage', 'flash sale',)
        G.add_edge('HomePage', 'Profile member',)
        G.add_edge('HomePage', 'Messenger',)
        G.add_edge('HomePage', 'Help',)
        G.add_edge('HomePage', 'SeachProduct',)
        G.add_edge('HomePage', 'RecommentProduct',)
        G.add_edge('HomePage', 'Cart',)

        G.add_edge('Login', 'HomePage',)
        G.add_edge('Login', 'Register',)

        G.add_edge('Register', 'Login',)
        G.add_edge('Register', 'HomePage',)

        G.add_edge('FollowProduct', 'LastOreder',)
        G.add_edge('FollowProduct', 'HomePage',)

        G.add_edge('ReccommentShop', 'Cart',)
        G.add_edge('ReccommentShop', 'HomePage',)

        G.add_edge('flash sale', 'Cart',)
        G.add_edge('flash sale', 'HomePage',)

        G.add_edge('Profile member', 'Order',)
        G.add_edge('Profile member', 'Logout',)
        G.add_edge('Profile member', 'Favorite',)
        G.add_edge('Profile member', 'CancellationReturn',)
        G.add_edge('Profile member', 'ManageProfile',)
        G.add_edge('Profile member', 'HomePage',)

        G.add_edge('Help', 'HomePage',)
        G.add_edge('Help', 'FollowProduct',)

        G.add_edge('Messenger', 'HomePage',)


        G.add_edge('product coupons', 'HomePage',)

        G.add_edge('SeachProduct', 'HomePage',)
        G.add_edge('SeachProduct', 'ReccommentShop',)
        G.add_edge('SeachProduct', 'RecommentProduct',)

        G.add_edge('RecommentProduct', 'HomePage',)
        G.add_edge('RecommentProduct', 'Cart',)
        G.add_edge('RecommentProduct', 'flash sale',)

        G.add_edge('Cart', 'HomePage',)
        G.add_edge('Cart', 'RecommentProduct',)
        G.add_edge('Cart', 'SeachPRoduct',)
        G.add_edge('Cart', 'Messenger',)
        G.add_edge('Cart', 'Profile member',)
        G.add_edge('Cart', 'product coupons',)


        # พล็อตกราฟและระบุทิศทางของ edge
        fig, ax = plt.subplots(figsize=(15, 12)) # กำหนดขนาดของกราฟ
        pos = nx.kamada_kawai_layout(G)  # เปลี่ยน layout เป็น 'circular'
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos, font_size=10)  # เปลี่ยนขนาด font เป็น 12
        nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
                # ระบุจุดเริ่มและสิ้นสุด
        startPoint = str(input("Enter start point:"))
        endPoint = str(input("Enter end point:"))

        # ระบุจุดจากที่หนึ่งไปยังอีกที่ว่าผ่านจุดใดบ้าง
        path = nx.shortest_path(G, startPoint, endPoint)
        print(path)

        path = nx.shortest_path(G, source=startPoint, target=endPoint)

        # แสดงกราฟที่ระบุเส้นทางแล้ว
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, edge_color='gray')  # ให้สีเส้นเป็นสีเทา
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

        # เปลี่ยนสีของเส้นทางที่ผ่านไปทั้งหมดใน path เป็นสีแดง
        for i in range(len(path)-1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2.0)
        plt.show()
    def Grahp3random_layout():#วางโหนดแบบสุ่ม
        import networkx as nx
        import matplotlib.pyplot as plt

        # สร้างกราฟ
        G = nx.DiGraph()

        # เพิ่ม vertex
        G.add_node('HomePage')
        G.add_node('Register')
        G.add_node('FollowProduct')
        G.add_node('ReccommentShop')
        G.add_node('flash sale')
        G.add_node('Profile member')
        G.add_node('Messenger')
        G.add_node('Help')
        G.add_node('product coupons')
        G.add_node('SeachProduct')
        G.add_node('RecommentProduct')
        G.add_node('LastOreder')
        G.add_node('Cart')
        G.add_node('Order')
        G.add_node('Favorite')
        G.add_node('CancellationReturn')
        G.add_node('ManageProfile')

        # เพิ่ม edge และระบุทิศทาง
        G.add_edge('HomePage', 'Login',)
        G.add_edge('HomePage', 'ReccommentShop',)
        G.add_edge('HomePage', 'flash sale',)
        G.add_edge('HomePage', 'Profile member',)
        G.add_edge('HomePage', 'Messenger',)
        G.add_edge('HomePage', 'Help',)
        G.add_edge('HomePage', 'SeachProduct',)
        G.add_edge('HomePage', 'RecommentProduct',)
        G.add_edge('HomePage', 'Cart',)

        G.add_edge('Login', 'HomePage',)
        G.add_edge('Login', 'Register',)

        G.add_edge('Register', 'Login',)
        G.add_edge('Register', 'HomePage',)

        G.add_edge('FollowProduct', 'LastOreder',)
        G.add_edge('FollowProduct', 'HomePage',)

        G.add_edge('ReccommentShop', 'Cart',)
        G.add_edge('ReccommentShop', 'HomePage',)

        G.add_edge('flash sale', 'Cart',)
        G.add_edge('flash sale', 'HomePage',)

        G.add_edge('Profile member', 'Order',)
        G.add_edge('Profile member', 'Logout',)
        G.add_edge('Profile member', 'Favorite',)
        G.add_edge('Profile member', 'CancellationReturn',)
        G.add_edge('Profile member', 'ManageProfile',)
        G.add_edge('Profile member', 'HomePage',)

        G.add_edge('Help', 'HomePage',)
        G.add_edge('Help', 'FollowProduct',)

        G.add_edge('Messenger', 'HomePage',)


        G.add_edge('product coupons', 'HomePage',)

        G.add_edge('SeachProduct', 'HomePage',)
        G.add_edge('SeachProduct', 'ReccommentShop',)
        G.add_edge('SeachProduct', 'RecommentProduct',)

        G.add_edge('RecommentProduct', 'HomePage',)
        G.add_edge('RecommentProduct', 'Cart',)
        G.add_edge('RecommentProduct', 'flash sale',)

        G.add_edge('Cart', 'HomePage',)
        G.add_edge('Cart', 'RecommentProduct',)
        G.add_edge('Cart', 'SeachPRoduct',)
        G.add_edge('Cart', 'Messenger',)
        G.add_edge('Cart', 'Profile member',)
        G.add_edge('Cart', 'product coupons',)


        # พล็อตกราฟและระบุทิศทางของ edge
        fig, ax = plt.subplots(figsize=(15, 12)) # กำหนดขนาดของกราฟ
        pos = nx.random_layout(G)  # เปลี่ยน layout เป็น 'circular'
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos, font_size=10)  # เปลี่ยนขนาด font เป็น 12
        nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
                # ระบุจุดเริ่มและสิ้นสุด
        startPoint = str(input("Enter start point:"))
        endPoint = str(input("Enter end point:"))

        # ระบุจุดจากที่หนึ่งไปยังอีกที่ว่าผ่านจุดใดบ้าง
        path = nx.shortest_path(G, startPoint, endPoint)
        print(path)

        path = nx.shortest_path(G, source=startPoint, target=endPoint)

        # แสดงกราฟที่ระบุเส้นทางแล้ว
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, edge_color='gray')  # ให้สีเส้นเป็นสีเทา
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

        # เปลี่ยนสีของเส้นทางที่ผ่านไปทั้งหมดใน path เป็นสีแดง
        for i in range(len(path)-1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2.0)
        plt.show()
    def Grahp4shell_layout():#วางโหนดตามแนววงศ์
        import networkx as nx
        import matplotlib.pyplot as plt

        # สร้างกราฟ
        G = nx.DiGraph()

        # เพิ่ม vertex
        G.add_node('HomePage')
        G.add_node('Register')
        G.add_node('FollowProduct')
        G.add_node('ReccommentShop')
        G.add_node('flash sale')
        G.add_node('Profile member')
        G.add_node('Messenger')
        G.add_node('Help')
        G.add_node('product coupons')
        G.add_node('SeachProduct')
        G.add_node('RecommentProduct')
        G.add_node('LastOreder')
        G.add_node('Cart')
        G.add_node('Order')
        G.add_node('Favorite')
        G.add_node('CancellationReturn')
        G.add_node('ManageProfile')

        # เพิ่ม edge และระบุทิศทาง
        G.add_edge('HomePage', 'Login',)
        G.add_edge('HomePage', 'ReccommentShop',)
        G.add_edge('HomePage', 'flash sale',)
        G.add_edge('HomePage', 'Profile member',)
        G.add_edge('HomePage', 'Messenger',)
        G.add_edge('HomePage', 'Help',)
        G.add_edge('HomePage', 'SeachProduct',)
        G.add_edge('HomePage', 'RecommentProduct',)
        G.add_edge('HomePage', 'Cart',)

        G.add_edge('Login', 'HomePage',)
        G.add_edge('Login', 'Register',)

        G.add_edge('Register', 'Login',)
        G.add_edge('Register', 'HomePage',)

        G.add_edge('FollowProduct', 'LastOreder',)
        G.add_edge('FollowProduct', 'HomePage',)

        G.add_edge('ReccommentShop', 'Cart',)
        G.add_edge('ReccommentShop', 'HomePage',)

        G.add_edge('flash sale', 'Cart',)
        G.add_edge('flash sale', 'HomePage',)

        G.add_edge('Profile member', 'Order',)
        G.add_edge('Profile member', 'Logout',)
        G.add_edge('Profile member', 'Favorite',)
        G.add_edge('Profile member', 'CancellationReturn',)
        G.add_edge('Profile member', 'ManageProfile',)
        G.add_edge('Profile member', 'HomePage',)

        G.add_edge('Help', 'HomePage',)
        G.add_edge('Help', 'FollowProduct',)

        G.add_edge('Messenger', 'HomePage',)


        G.add_edge('product coupons', 'HomePage',)

        G.add_edge('SeachProduct', 'HomePage',)
        G.add_edge('SeachProduct', 'ReccommentShop',)
        G.add_edge('SeachProduct', 'RecommentProduct',)

        G.add_edge('RecommentProduct', 'HomePage',)
        G.add_edge('RecommentProduct', 'Cart',)
        G.add_edge('RecommentProduct', 'flash sale',)

        G.add_edge('Cart', 'HomePage',)
        G.add_edge('Cart', 'RecommentProduct',)
        G.add_edge('Cart', 'SeachPRoduct',)
        G.add_edge('Cart', 'Messenger',)
        G.add_edge('Cart', 'Profile member',)
        G.add_edge('Cart', 'product coupons',)


        # พล็อตกราฟและระบุทิศทางของ edge
        fig, ax = plt.subplots(figsize=(15, 12)) # กำหนดขนาดของกราฟ
        pos = nx.shell_layout(G)  # เปลี่ยน layout เป็น 'circular'
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos, font_size=10)  # เปลี่ยนขนาด font เป็น 12
        nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
                # ระบุจุดเริ่มและสิ้นสุด
        startPoint = str(input("Enter start point:"))
        endPoint = str(input("Enter end point:"))

        # ระบุจุดจากที่หนึ่งไปยังอีกที่ว่าผ่านจุดใดบ้าง
        path = nx.shortest_path(G, startPoint, endPoint)
        print(path)

        path = nx.shortest_path(G, source=startPoint, target=endPoint)

        # แสดงกราฟที่ระบุเส้นทางแล้ว
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, edge_color='gray')  # ให้สีเส้นเป็นสีเทา
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

        # เปลี่ยนสีของเส้นทางที่ผ่านไปทั้งหมดใน path เป็นสีแดง
        for i in range(len(path)-1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2.0)
        plt.show()

    def Display(): #แสดงโมดูลทั้งหมด
        print(records)
    def Search():#แสดงว่าโมดูลดังกล่าวเชื่อมต่อกับโมดูลใดบ้าง
        search = input('Please Search Module: ')
        print(records.get(search))
    def Add():#เพิ่มโมดูลใน records
        Display()
        MainModule = input('Add Enter MainModule: ')
        SubModule = input('Add Enter SubModule: ')
        if MainModule in records:
            records[MainModule].append(SubModule)
        else:
            records.update({MainModule: [SubModule]})
            
        while True:
            choice = input("Do you want to add more SubModule to this MainModule? (y/n): ").lower()
            if choice == "y":
                SubModule = input("Enter value: ")
                records[MainModule].append(SubModule)  # เพิ่ม value ใน list ของ key
            else:
                break
            print(records)
    def Modifier():#ปรับแต่งโมดูลต่างๆได้
        Display()
        addKey = input('Modifier Enter ID: ')
        addName = input('Modifier Enter Name: ')
        addMail = input('Modifier Enter Email: ')
        addPhone = input('Modifier Enter Phone Number: ')
        records[addKey] = addName , addMail , addPhone
        print(records)
    def Del():#ลบโมดูลต่างๆได้
        addKey = input('Delete Enter ID: ')
        records.pop(addKey)
        print(records)
    def Exits():#ตรวจสอบว่ามีโมดูลชื่อนี้ไหม
        name = input('Exits Module : ')     
        if(name in records ):
            print(name , 'found index = ')
            Display()
        if(name not in records):
            print(name , 'not found')
            Display()    

    def main1():
        keep = 'y' 
        while keep == 'y' :
            print('1.Display Module Function')
            print('2.Search Module Function')
            print('3.Add Module Function')
            print('4.Modifier Module Function')
            print('5.Delete Module Function')
            print('6.Exist Funtion')
            Select = int(input('Please Seclect Funtion : '))
            
            if Select == 1:
                Display()
            elif Select == 2:
                Search()
            elif Select == 3:
                Add()
            elif Select == 4:
                Modifier()
            elif Select == 5:
                Del()
            elif Select == 6:
                Exits()
            else:
                print('อย่าเปรี้ยวไอสัสพิมพ์ดีๆ')
                
            keep = input('Enter y for Moretime Enter n for Exit Admin: ').lower()

    def main2():
        keep = 'y'
        while keep == 'y':
            print('1.Display Module Function')
            print('2.Search Module Function')
            print('3.Exist Funtion')
            print('4.Grahp Funtion')
            
            Select = int(input('Please Seclect Funtion : '))
            
            if Select == 1:
                Display()
            elif Select == 2:
                Search()
            elif Select == 3:
                Exits()
            elif Select == 4:
                Grahp()
            else:
                print('อย่าเปรี้ยวไอสัสพิมพ์ดีๆ')
                
            keep = input('Enter y for Moretime Enter n for Exit left Client: ').lower()

    def main():
        keep = 'y'
        while keep == 'y':
            print('1.Admin')
            print('2.Client')

            Select = int(input('Please Select Funtion : '))
            
            if Select == 1:
                main1()
            elif Select == 2:
                main2()
            else:
                print('อย่าเปรี้ยวไอสัสพิมพ์ดีๆ')
                
            keep = input('Enter y for Moretime Enter n for Exit left Admin/Client: ').lower()
    main()
    
Bigkuma()
