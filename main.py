import json
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup


class CredyMarket(App):

    def build(self):
        self.products = []
        self.load_products()

        self.sm = ScreenManager()

        # =========================
        # ACCUEIL
        # =========================
        home = Screen(name="home")

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="CREDY MARKET",
            font_size=32,
            bold=True,
            size_hint_y=None,
            height=70
        )

        subtitle = Label(
            text="Isoko ryo kuri telefone",
            font_size=18,
            size_hint_y=None,
            height=50
        )

        btn_products = Button(
            text="🛍️ RABA IBICURUZWA",
            font_size=20,
            size_hint_y=None,
            height=65
        )

        btn_add = Button(
            text="➕ SHIRAHO IKICURUZWA",
            font_size=20,
            size_hint_y=None,
            height=65
        )

        btn_profile = Button(
            text="👤 PROFIL YANJE",
            font_size=20,
            size_hint_y=None,
            height=65
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(btn_products)
        layout.add_widget(btn_add)
        layout.add_widget(btn_profile)

        home.add_widget(layout)

        btn_products.bind(
            on_press=lambda x: self.show_products()
        )

        btn_add.bind(
            on_press=lambda x: setattr(
                self.sm, "current", "add"
            )
        )

        # =========================
        # SHIRAHO IKICURUZWA
        # =========================
        add = Screen(name="add")

        add_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        add_title = Label(
            text="SHIRAHO IKICURUZWA",
            font_size=26,
            bold=True,
            size_hint_y=None,
            height=60
        )

        self.product_name = TextInput(
            hint_text="Izina ry'ikicuruzwa",
            multiline=False,
            size_hint_y=None,
            height=55
        )

        self.price = TextInput(
            hint_text="Igiciro (FBu)",
            multiline=False,
            input_filter="int",
            size_hint_y=None,
            height=55
        )

        self.phone = TextInput(
            hint_text="Numero ya telefone",
            multiline=False,
            input_filter="int",
            size_hint_y=None,
            height=55
        )

        self.description = TextInput(
            hint_text="Insiguro y'ikicuruzwa",
            multiline=True,
            size_hint_y=None,
            height=120
        )

        save_btn = Button(
            text="💾 BIKA IKICURUZWA",
            font_size=19,
            size_hint_y=None,
            height=65
        )

        back_btn = Button(
            text="⬅️ SUBIRA",
            size_hint_y=None,
            height=55
        )

        add_layout.add_widget(add_title)
        add_layout.add_widget(self.product_name)
        add_layout.add_widget(self.price)
        add_layout.add_widget(self.phone)
        add_layout.add_widget(self.description)
        add_layout.add_widget(save_btn)
        add_layout.add_widget(back_btn)

        add.add_widget(add_layout)

        save_btn.bind(
            on_press=lambda x: self.save_product()
        )

        back_btn.bind(
            on_press=lambda x: setattr(
                self.sm, "current", "home"
            )
        )

        # =========================
        # IBICURUZWA
        # =========================
        products = Screen(name="products")

        self.products_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        products.add_widget(self.products_layout)

        # =========================
        # SCREEN MANAGER
        # =========================
        self.sm.add_widget(home)
        self.sm.add_widget(add)
        self.sm.add_widget(products)

        return self.sm

    # =========================
    # FILE YO KUBIKAMWO
    # =========================

    def get_file(self):
        return os.path.join(
            self.user_data_dir,
            "credy_market_data.json"
        )

    # =========================
    # KUBIKA MURI TELEFONE
    # =========================

    def save_products(self):
        try:
            with open(
                self.get_file(),
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    self.products,
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        except Exception as e:
            print("Erreur:", e)

    # =========================
    # GUSOMA IVYABITSWE
    # =========================

    def load_products(self):
        try:
            if os.path.exists(self.get_file()):
                with open(
                    self.get_file(),
                    "r",
                    encoding="utf-8"
                ) as file:
                    self.products = json.load(file)
            else:
                self.products = []
        except Exception as e:
            print("Erreur:", e)
            self.products = []

    # =========================
    # BIKA IKICURUZWA
    # =========================

    def save_product(self):

        name = self.product_name.text.strip()
        price = self.price.text.strip()
        phone = self.phone.text.strip()
        description = self.description.text.strip()

        if not name:
            self.show_message(
                "Ikosa",
                "Andika izina ry'ikicuruzwa."
            )
            return

        if not price:
            self.show_message(
                "Ikosa",
                "Andika igiciro."
            )
            return

        if not phone:
            self.show_message(
                "Ikosa",
                "Andika numero ya telefone."
            )
            return

        product = {
            "name": name,
            "price": price,
            "phone": phone,
            "description": description
        }

        self.products.append(product)

        self.save_products()

        self.product_name.text = ""
        self.price.text = ""
        self.phone.text = ""
        self.description.text = ""

        self.show_message(
            "Birakunze ✅",
            "Ikicuruzwa cawe cabitswe neza!"
        )

    # =========================
    # RABA IBICURUZWA
    # =========================

    def show_products(self):

        self.products_layout.clear_widgets()

        title = Label(
            text="🛍️ IBICURUZWA",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=60
        )

        self.products_layout.add_widget(title)

        if not self.products:

            empty = Label(
                text="Nta bicuruzwa birabikwa.",
                font_size=18
            )

            self.products_layout.add_widget(empty)

        else:

            scroll = ScrollView()

            list_layout = BoxLayout(
                orientation="vertical",
                spacing=10,
                size_hint_y=None,
                padding=5
            )

            list_layout.bind(
                minimum_height=list_layout.setter(
                    "height"
                )
            )

            for product in self.products:

                text = (
                    "🛍️ " + product["name"]
                    + "\n💰 " + product["price"] + " FBu"
                    + "\n📞 " + product["phone"]
                    + "\n📝 " + product["description"]
                )

                item = Label(
                    text=text,
                    font_size=17,
                    size_hint_y=None,
                    height=130
                )

                list_layout.add_widget(item)

            scroll.add_widget(list_layout)

            self.products_layout.add_widget(scroll)

        back = Button(
            text="⬅️ SUBIRA",
            size_hint_y=None,
            height=55
        )

        self.products_layout.add_widget(back)

        back.bind(
            on_press=lambda x: setattr(
                self.sm,
                "current",
                "home"
            )
        )

        self.sm.current = "products"

    # =========================
    # MESSAGE
    # =========================

    def show_message(self, title, message):

        content = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        label = Label(
            text=message,
            font_size=18
        )

        button = Button(
            text="OK",
            size_hint_y=None,
            height=50
        )

        content.add_widget(label)
        content.add_widget(button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.85, 0.4)
        )

        button.bind(
            on_press=popup.dismiss
        )

        popup.open()


if __name__ == "__main__":
    CredyMarket().run()