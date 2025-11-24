import requests
from bs4 import BeautifulSoup
from db.models import SessionLocal, Senator, Committee, senator_committee
from sqlalchemy import insert

BASE_URL = "https://www.senate.gov/committees/index.htm"


def fetch_committees():
    resp = requests.get(BASE_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # TODO: adjust selectors to match senate.gov structure
    committee_blocks = soup.select("div.committee")  # placeholder

    data = []
    for block in committee_blocks:
        name = block.select_one("h3").get_text(strip=True)
        chamber = "Senate"
        code = block.get("id")  # or however the code appears

        members = []
        for li in block.select("ul.members li"):
            full_name = li.get_text(strip=True)
            members.append(full_name)

        data.append({"name": name, "chamber": chamber, "code": code, "members": members})

    return data


def upsert_committees(data):
    db = SessionLocal()
    try:
        for c in data:
            committee = db.query(Committee).filter_by(code=c["code"]).one_or_none()
            if not committee:
                committee = Committee(name=c["name"], chamber=c["chamber"], code=c["code"])
                db.add(committee)
                db.flush()

            for member_name in c["members"]:
                senator = db.query(Senator).filter_by(full_name=member_name).one_or_none()
                if not senator:
                    senator = Senator(full_name=member_name)
                    db.add(senator)
                    db.flush()

                # raw INSERT into senator_committee junction
                db.execute(
                    insert(senator_committee).values(
                        senator_id=senator.senator_id,
                        committee_id=committee.committee_id,
                        role=None,
                        start_date=None,
                        end_date=None,
                    ).on_conflict_do_nothing()
                )
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    committees = fetch_committees()
    upsert_committees(committees)
