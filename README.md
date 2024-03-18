from earth import Human

class ItMe(Human):
    first_name: str = "Ayman"
    last_name: str = "Mujahid"
    work_where: str = "SBS"
    work_what: str = "backend-engineer"

    @classmethod
    def hi(cls):
        print(f"hey 👋, i'm {cls.first_name.capitalize()}")
        print(f"currently i work in {cls.work_what} @ {cls.work_where}")

>>> ItMe.hi()
hey 👋, i'm Joon Hwan
currently i work in backend-engineer @ SBS
