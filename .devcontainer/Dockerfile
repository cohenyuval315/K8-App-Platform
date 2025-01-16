FROM ubuntu:latest

# ---------- WORKSPACE ----------
ARG WORKSPACE
ARG HOME_DIR
ARG GROUP
ARG GROUP_ID
ARG USER
ARG USER_ID
ARG USER_PASSWORD



ENV HOME=${HOME_DIR}/${USER}

WORKDIR ${HOME}

ENV USER_WORKSPACE=${HOME_DIR}/${USER}/${WORKSPACE}

RUN mkdir -p ${USER_WORKSPACE}


# ---------- USER ----------


RUN groupadd -g ${GROUP_ID} ${GROUP}
RUN useradd -m -s /bin/bash -u ${USER_ID} -g ${GROUP} ${USER}

RUN chown -R ${USER} ${USER_WORKSPACE}
RUN echo ${USER}:${USER_PASSWORD} | chpasswd

# ---------- ESSENTIAL ----------

# Install general dependencies (tools commonly used in development)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    sudo \
    vim \
    dpkg-dev \
    flex \
    bison \
    dpkg \
    nano \
    gcc \
    make \
    cmake \
    cmake-data \
    g++ \
    gfortran \
    tree \
    patch \
    sed \
    yq \
    jq \
    subversion \
    net-tools \
    nmap \
    tar \
    unzip \
    gzip \
    llvm \
    bash-completion \
    ca-certificates \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*



# -------- DEPS  --------

# TODO spit by Python-specific dependencies (necessary for pyenv and Python installation)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libreadline-dev \
    zlib1g-dev \
    libbz2-dev \
    libsqlite3-dev \
    libncurses5-dev \
    # libncursesw5-dev \
    # ncurses-dev \
    # util-linux-dev \
    # zlib-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libgdbm-dev \
    # gdbm-dev \
    libtirpc-dev \
    libc-dev \
    libnsl-dev \
    # mecab-ipadic-utf8 \
    # openssl-dev \
    libnss3-dev \
    libnss3-tools \
    libxmlsec1-dev \
    libxml2-dev \
    libffi-dev \
    # libtool \
    xz-utils \
    # tk-dev \
    liblzma-dev \
    python3-dev \
    # python3-openssl \
    && rm -rf /var/lib/apt/lists/*


# -------- PYTHON --------

ARG PYTHON_VERSION
ARG PYTHON_PATH

ENV PYTHONPATH=${PYTHON_PATH}
ENV PYTHON_VERSION=${PYTHON_VERSION}

# ---------- UV ----------

# Install uv - An extremely fast Python package and project manager
RUN sudo apt update
RUN curl -LsSf https://astral.sh/uv/install.sh | sh


# ---------- PIPX ----------

# Install pipx
RUN sudo apt update
RUN sudo apt install -y pipx
RUN sudo pipx ensurepath


# ---------- PYENV ----------

    # RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
# RUN echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
# RUN echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

# Configure pyenv in the shell
# RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc \
#     && echo 'eval "$(pyenv init --path)"' >> ~/.bashrc \
#     && echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
#     && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc


# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
# echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
# echo 'eval "$(pyenv init - bash)"' >> ~/.profile

# Install a specific version of Python using pyenv

# Install pyenv
RUN sudo apt update
RUN curl -fsSL https://pyenv.run | bash

ENV PYENV_ROOT=${HOME}/.pyenv
ENV PATH=${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
RUN pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}
RUN pyenv rehash






# ---------- USER ----------
WORKDIR ${USER_WORKSPACE}

# ---------- INSTALL DEPENDANCIES ----------
# Install required Python packages


RUN pip install uv
# RUN uv self update

# COPY pyproject.toml ./
# RUN uv pip install --all-extras .
# uv pip compile pyproject.toml > requirements.txt
# uv pip sync -r requirements.txt
# RUN bash -c "source ~/.bashrc && pip install --no-cache-dir -r requirements.txt"

# RUN pip install --no-cache-dir -r requirements.txt




USER ${USER}

# ---------- ENTRY ----------

CMD ["/bin/bash"]
