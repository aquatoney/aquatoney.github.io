FROM ruby:3.4.5-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git libyaml-dev nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /srv/jekyll
ENV BUNDLE_PATH=/usr/local/bundle \
    JEKYLL_ENV=development

COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v 4.0.6 --no-document && bundle install

EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--config", "_config.yml,_config.local.yml", "--host", "0.0.0.0", "--force_polling", "--destination", "/tmp/_site"]
