import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def question1(data):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(
        data,
        autopct="%1.1f%%",
        labels=["Casual", "Registered"],
        wedgeprops={"width": 0.4},
        pctdistance=1.3,
    )
    ax.legend(["Casual", "Registered"], bbox_to_anchor=(1.1, 0.9), framealpha=0)

    return fig


def question2(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap="coolwarm", fmt=".2f")
    return fig


def question3(data):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(25, 5))

    ax1.barh(
        y="dteday",
        width="cnt",
        data=data.sort_values(by="cnt", ascending=False).head(),
        color="skyblue",
    )
    ax1.set_title("Penyewa Tertinggi")
    ax1.invert_yaxis()
    ax1.set_xticks(range(0, 9500, 500))

    ax2.barh(
        y="dteday",
        width="cnt",
        data=data.sort_values(by="cnt").head(),
        color="salmon",
    )
    ax2.invert_xaxis()
    ax2.yaxis.set_label_position("right")
    ax2.yaxis.tick_right()
    ax2.set_title("Penyewa Terendah")
    ax2.invert_yaxis()
    ax2.set_xticks(range(0, 700, 50))

    return fig


def question4(data):
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.plot(data["month"], data["cnt"], marker="o")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah")
    ax.set_xticks(
        data["month"],
        labels=data["month"].dt.strftime("%Y-%m"),
    )
    fig.tight_layout()
    return fig


def question5a(data):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.barh(
        data["mnth"],
        data["casual"],
        left=data["registered"],
        label="Casual",
    )
    ax.barh(data["mnth"], data["registered"], label="Registered")

    ax.set_title("Distribusi Penyewa Sepeda Berdasarkan Bulan", fontsize=15, pad=30)
    ax.set_ylabel("Bulan")
    ax.set_xlabel("Jumlah")
    ax.invert_yaxis()
    ax.legend(bbox_to_anchor=(1, 1.1), ncol=2)

    return fig


def question5b(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(
        data["weekday"],
        data["casual"],
        left=data["registered"],
        label="Casual",
    )
    ax.barh(data["weekday"], data["registered"], label="Registered")

    ax.set_title("Distribusi Penyewa Sepeda Berdasarkan Hari", pad=30, fontsize=15)
    ax.set_ylabel("Hari")
    ax.set_xlabel("Jumlah")
    ax.invert_yaxis()
    days_ = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    ax.set_yticks(data["weekday"], labels=days_)
    ax.legend(bbox_to_anchor=(1, 1.1), ncol=2)

    return fig


def question5c(data):
    fig, ax = plt.subplots(figsize=(20, 5))

    ax.bar(
        data["hr"],
        data["casual"],
        bottom=data["registered"],
        label="Casual",
    )
    ax.bar(data["hr"], data["registered"], label="Registered")

    ax.set_title("Distribusi Penyewa Sepeda Berdasarkan Jam", fontsize=15, pad=30)
    ax.set_ylabel("Jumlah")
    ax.set_xlabel("Jam")
    ax.set_xticks(data["hr"], [f"{time}:00" for time in data["hr"]])
    ax.legend(bbox_to_anchor=(1, 1.1), ncol=2)

    return fig


def question5d(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(
        data["season"],
        data["casual"],
        bottom=data["registered"],
        label="Casual",
    )
    ax.bar(data["season"], data["registered"], label="Registered")

    ax.set_title("Distribusi Penyewa Sepeda Berdasarkan Musim", fontsize=15, pad=30)
    ax.set_ylabel("Jumlah")
    ax.set_xlabel("Season")
    ax.set_xticks(data["season"], labels=["Springer", "Summer", "Fall", "Winter"])
    ax.legend(bbox_to_anchor=(1, 1.1), ncol=2)

    return fig


def question5e(data):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        data["weathersit"],
        data["casual"],
        bottom=data["registered"],
        label="Casual",
    )
    ax.bar(data["weathersit"], data["registered"], label="Registered")

    ax.set_title("Distribusi Penyewa Sepeda Berdasarkan Cuaca", fontsize=15, pad=30)
    ax.set_ylabel("Jumlah")
    ax.set_xlabel("Hari")
    ax.set_xticks(data["weathersit"], ["Clear", "Cloudy", "Rain", "Heavy Rain"])
    ax.legend(bbox_to_anchor=(1, 1.1), ncol=2)

    return fig


def time_series_decomposition(data):
    return seasonal_decompose(data["cnt"], model="multiplicative").plot()
