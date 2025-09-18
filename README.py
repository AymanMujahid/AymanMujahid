from earth import Human

class ItMe(Human):
    def __init__(self,
                 first_name: str = "Ayman",
                 last_name: str = "Mujahid",
                 work_where: str = "SBS",
                 work_what: str = (
                     "Software Engineer – Back-End & Generative AI Focused | "
                     "Passionate About Building with Generative AI | "
                     "Exploring Intelligent Solutions")):
        self.first_name = first_name
        self.last_name = last_name
        self.work_where = work_where
        self.work_what = work_what

    def hi(self):
        print(f"hey 👋, i'm {self.first_name.capitalize()} {self.last_name.capitalize()}")
        print(f"currently i work in {self.work_what} @ {self.work_where}")

me = ItMe()
me.hi()


hey 👋, i'm Ayman Mujahid
currently i work in Software Engineer – Back-End & Generative AI Focused | Passionate About Building with Generative AI | Exploring Intelligent Solutions @ SBS
